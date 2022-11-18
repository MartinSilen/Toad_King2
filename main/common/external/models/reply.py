from dataclasses import dataclass, field

@dataclass
class Reply:
    external_id: str
    contents: str
