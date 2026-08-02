
from ai_sdk.message import Message
from abc import abstractmethod
from abc import ABC
class LLMProvider(ABC):
    @abstractmethod
    def generate(self,history:list[Message],message:Message)->Message:
        pass
        