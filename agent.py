from langchain.agents import create_agent
from llm import get_llm
from tools import All_Tools

agent = create_agent(
    model=get_llm(provider="gemini"),
    tools=All_Tools,
    system_prompt=(
        "You are a helpful assistant that can perform mathematical "
        "operations and save notes to a file."
    ),
)