from agent import agent

question = input("Ask: ")

result = agent.invoke({
    "messages": [
        {"role": "user", "content": question}
    ]
})

print("\nAI:", result["messages"][-1].content)