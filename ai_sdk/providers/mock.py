
from collections.abc import Sequence
from ai_sdk.enums import Role
from ai_sdk.message import Message
from ai_sdk.providers.base import LLMProvider
class MockProvider(LLMProvider):
    def generate(self,history:Sequence[Message],message:str)->Message:
        return Message(Role.ASSISTANT,"Echo: "+message)
        
        