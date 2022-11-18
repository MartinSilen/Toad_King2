from datetime import datetime

from main.common.external.dao.dao_event import DaoEventImplementation
from main.common.external.dao.dao_location import DaoLocationImplementation
from main.common.external.dao.dao_reply import DaoReplyImplementation
from main.common.external.dao.dao_user import DaoUserImplementation
from main.common.external.models.event import Event
from main.common.external.models.game_object import GameObject
from main.common.external.models.location import Location
from main.common.external.models.reply import Reply
from main.common.external.models.user import User

default_event = Event(external_id='default_event', event_name='some_event', event_duration=1,
                      event_start_time=datetime.now(), event_descriptions=['test1', 'test2'])
default_user = User(external_id='test1', character_name='test_name')
default_game_object = GameObject(object_name='test_object', object_tags=['test1', 'test2'], object_descriptions=['test1'])
default_location = Location(external_id='test1', location_reply_names={'test1': 'test1', 'test2': 'test2'})
default_reply = Reply(external_id='test1', contents='This is test reply 1')
default_reply2 = Reply(external_id='test2', contents='This is test reply 2')

dao_events = DaoEventImplementation()
dao_location = DaoLocationImplementation()
dao_user = DaoUserImplementation()
dao_reply = DaoReplyImplementation()

