from app.services.openai_client import client
from app.agent.executor import execute_tool
from app.memory.memory_store import load_memory, save_memory
import os


def run_agent(user_input: str):

    # Tool: calculator
    if any(op in user_input for op in ["+", "-", "*", "/"]):
        return execute_tool("calculate", user_input)

    # Load memory
    memory = load_memory()

    # Keep only last 10 messages (5 exchanges)
    memory = memory[-10:]

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    messages.extend(memory)

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=messages,
        max_tokens=300,
        temperature=0.3
    )

    assistant_reply = response.choices[0].message.content

    # Save memory
    memory.append({"role": "user", "content": user_input})
    memory.append({"role": "assistant", "content": assistant_reply})

    save_memory(memory)

    return assistant_reply