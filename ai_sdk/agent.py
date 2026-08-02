from ai_sdk.providers.base import LLMProvider
from ai_sdk.message import Message
from dataclasses import dataclass
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
        llm_message=self.call_llm(message)
        self.messages.append(llm_message)
        return llm_message

    def call_llm(self,message:str)->Message:
        return self.provider.generate(self.history(),message)

    def history(self)->list[Message]:
        return list(self.messages)


