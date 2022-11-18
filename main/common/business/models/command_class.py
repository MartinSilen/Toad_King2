from dataclasses import dataclass, field


@dataclass
class Command:
    user_id: str
    command: str
    command_type: str = 'user'
    command_arguments: list = field(default_factory=list)
