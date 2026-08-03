

from dataclasses import dataclass
from ai_sdk.message import Message

@dataclass
class LLMResponse():
    """Response from the LLM."""
    message:Message