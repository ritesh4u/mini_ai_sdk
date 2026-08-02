
from collections.abc import Sequence
from ai_sdk.message import Message
from abc import ABC, abstractmethod
class LLMProvider(ABC):
    """Base interface for all LLM providers."""
    @abstractmethod
    def generate(self,history:Sequence[Message],message:str)->Message:
        pass
        