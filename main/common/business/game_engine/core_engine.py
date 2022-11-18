import os
from dotenv import load_dotenv
from main.common.abstracts.IOsystem.response_dispatcher import ResponseDispatcherInterface
from main.common.business.services.location_service import LocationServiceImplementation
from main.common.business.services.reply_service import ReplyServiceImplementation
from main.common.business.services.user_service import UserServiceImplementation
from main.common.external.models.entity_with_position import PositionalEntity
from main.common.external.models.location import Location
from main.common.external.models.user import User
from main.common.business.IOsystem.response_factory import construct_response

class CoreEngine:

    def __init__(self, user_service: UserServiceImplementation, location_service: LocationServiceImplementation,
                 reply_service: ReplyServiceImplementation, response_dispatcher: ResponseDispatcherInterface):
        load_dotenv()
        self.user_service = user_service
        self.location_service = location_service
        self.reply_service = reply_service
        self.response_dispatcher = response_dispatcher

    def _can_move_to(self, moving_object: PositionalEntity, target_location: Location):
        origin_location = self.location_service.get_location(moving_object.position)
        if isinstance(moving_object, User):
            if 'cant_move' not in moving_object.character_status and origin_location.external_id in \
                    target_location.connected_location_names:
                return True
        elif origin_location.external_id in target_location.connected_location_names:
            return True
        else:
            return False

    def _write_to_database(self, users=None, locations=None, events=None):
        for user in users:
            self.user_service.update_user(user)
        for location in locations:
            self.location_service.update_location(location)

    def _move_user(self, user: User, target_location: Location):
        user_location = self.location_service.get_location(user.position)
        if self._can_move_to(user, target_location):
            if user.external_id in user_location.visiting_user_ids:
                user_location.visiting_user_ids.remove(user.external_id)
            target_location.visiting_user_ids.append(user.external_id)
            user.position = target_location.external_id
            self.response_dispatcher.send_response(response=construct_response(user.external_id,
                                                                               target_location.location_reply_names['welcome']))
            self._write_to_database([user], [user_location, target_location])
        else:
            if 'cant_move' in user.character_status:
                self.response_dispatcher.send_response(response=construct_response(user.external_id, 'stuck'))
            else:
                self.response_dispatcher.send_response(response=construct_response(user.external_id, 'no_way'))

    def display_character_info(self, user: User):
        self.response_dispatcher.send_response(response=construct_response(user.external_id, additional_text=str(user)))

    def move_to_location(self, moving_object: PositionalEntity, move_target: str):
        move_target = self.location_service.get_location(move_target)
        if isinstance(moving_object, User):
            self._move_user(moving_object, move_target)
        else:
            self.response_dispatcher.send_response(construct_response(os.getenv('ADMIN_USER_ID'),
                                                                      f'Wrong object tried moving: {str(moving_object)}'))

    def invalid_command_response(self, user: User):
        self.response_dispatcher.send_response(response=construct_response(user.external_id, 'invalid_command'))

