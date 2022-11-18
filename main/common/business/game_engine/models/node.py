from dataclasses import dataclass
from typing import Any

from main.common.business.game_engine.models.place import Place


@dataclass
class Node:
    coordinate: int
    connections: list
    place: Place
