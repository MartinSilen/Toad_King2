from dataclasses import dataclass, field

from main.common.external.models.entity_with_position import PositionalEntity


@dataclass(kw_only=True)
class GameObject(PositionalEntity):
    object_name: str
    object_tags: list[str]
    object_descriptions: list[str]
    owner: str = None
