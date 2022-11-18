from dataclasses import dataclass, field


@dataclass
class Location:
    external_id: str
    visiting_user_ids: list = field(default_factory=list)
    objects: list = field(default_factory=list)
    connected_location_names: list = field(default_factory=list)
    location_info: dict = field(default_factory=dict)
    location_events: list = field(default_factory=list)
    location_reply_names: dict = field(default_factory=dict)
