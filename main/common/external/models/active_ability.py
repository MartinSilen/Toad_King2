import datetime
from dataclasses import dataclass


@dataclass
class ActiveAbility:
    ability_name: str
    cooldown: int = 0
    last_used: datetime.datetime = None
