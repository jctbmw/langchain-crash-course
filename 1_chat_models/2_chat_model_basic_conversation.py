from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequence of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="You are a realestate agent. A customer is asking you about housing in texas."),
    HumanMessage(content="What areas are affordable and growing in Texas?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="You are a realestate agent. A customer is asking you about housing in texas."),
    HumanMessage(content="What areas are affordable and growing in Texas?"),
    AIMessage(content="Austin is a popular city in Texas. It is known for its affordable housing and growing job market."),
    HumanMessage(content="What about Dallas?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
