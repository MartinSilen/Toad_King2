from dataclasses import dataclass, field
from main.common.external.models.active_ability import ActiveAbility
from main.common.external.models.entity_with_position import PositionalEntity


@dataclass(kw_only=True)
class User(PositionalEntity):
    external_id: str
    character_name: str
    character_active_abilities: [ActiveAbility] = None
    command_handler_name: str = None
    inactivity_counter: int = 0
    character_description: str = None
    character_race: str = None
    character_class: str = None
    character_status: list = field(default_factory=list)
    user_info: dict = field(default_factory=dict)

    def __str__(self):
        return f'Character Info: \n' \
               f'Name: {self.character_name} \n' \
               f'Race: {self.character_race} \n' \
               f'Class: {self.character_class} \n' \
               f'Description: {self.character_description} '

