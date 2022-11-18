from dataclasses import dataclass


@dataclass(kw_only=True)
class PositionalEntity:
    position: str = 'Limbo'