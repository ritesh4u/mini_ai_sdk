from ai_sdk.agent import Agent
from ai_sdk.providers.mock import MockProvider

mock_provider=MockProvider()
tutor_agent=Agent("Python Tutor","You teach Python",mock_provider)

tutor_agent.chat("Hello")
tutor_agent.chat("What is Python?")
# print(tutor_agent.history())

tutor_agent.stream()