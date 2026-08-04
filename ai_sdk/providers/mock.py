
from collections.abc import Iterator
from ai_sdk.llm_chunk import LLMChunk
from collections.abc import Sequence
from ai_sdk.message import Message
from ai_sdk.providers.base import LLMProvider
class MockProvider(LLMProvider):
    
    def stream(self,history:Sequence[Message])->Iterator[LLMChunk]:
        last =history[-1]
        last_index = len(last.content)-1
        for i,c in enumerate(last.content):
            yield LLMChunk(content=c,is_last=i==last_index)


        