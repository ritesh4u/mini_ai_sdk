
from dataclasses import dataclass
@dataclass
class LLMChunk:
    content:str
    is_last:bool=False