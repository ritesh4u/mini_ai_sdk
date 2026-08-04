from dataclasses import field
from ai_sdk.enums import Role
from datetime import datetime
from dataclasses import dataclass
@dataclass
class Message:
    role:Role
    content:str
    timestamp:str = field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))