
from ai_sdk.enums import Role
from ai_sdk.llm_chunk import LLMChunk
from collections.abc import Iterable
from ai_sdk.llm_response import LLMResponse
from collections.abc import Sequence
from ai_sdk.message import Message
from abc import ABC, abstractmethod
class LLMProvider(ABC):
    """Base interface for all LLM providers."""
    # @abstractmethod
    def generate(self,history:Sequence[Message])->LLMResponse:
        chunks=list(self.stream(history))
        
        return LLMResponse(Message(Role.ASSISTANT,"".join([c.content for c in chunks])))
    
    @abstractmethod
    def stream(self,history:Sequence[Message])->Iterable[LLMChunk]:
        pass
    
        