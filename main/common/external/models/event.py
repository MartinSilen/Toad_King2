import datetime
from dataclasses import dataclass

from main.common.external.models.entity_with_position import PositionalEntity


@dataclass(kw_only=True)
class Event(PositionalEntity):
    external_id: str
    event_name: str
    event_duration: int
    event_start_time: datetime.datetime
    event_descriptions: [str]
