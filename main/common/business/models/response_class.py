from dataclasses import dataclass


@dataclass
class Response:
    user_id: str
    message: str
