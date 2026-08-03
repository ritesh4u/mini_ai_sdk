from ai_sdk.llm_chunk import LLMChunk
from collections.abc import Iterator
from ai_sdk.providers.base import LLMProvider
from ai_sdk.message import Message
from ai_sdk.enums import Role

class Agent:
    name:str
    system_prompt:str
    messages:list[Message]
    provider:LLMProvider

    def __init__(self,name:str,system_prompt:str,provider:LLMProvider):
        self.name=name
        self.system_prompt=system_prompt
        self.messages=[Message(Role.SYSTEM,system_prompt)]
        self.provider=provider

    
    def chat(self,message:str)->Message:
        self.messages.append(Message(Role.USER,message))
        llm_response=self.provider.generate(self.history())
        self.messages.append(llm_response.message)
        return llm_response.message

    def stream(self)->Iterator[LLMChunk]:
        chunk=self.provider.stream(self.history())
        llm_chunk=[]
        for c in chunk:
            llm_chunk.append(c)
            yield c
        #combining chunks
        self.messages.append(Message(Role.ASSISTANT,"".join([c.content for c in llm_chunk])))
    
    
    def history(self)->list[Message]:
        return list(self.messages)


