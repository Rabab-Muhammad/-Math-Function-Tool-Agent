# import asyncio
# from decouple import config
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
# from agents.run import RunConfig



# gemini_api_key = config("GEMINI_API_KEY")

# if not gemini_api_key:
#     raise ValueError("🚨 GEMINI_API_KEY environment variable is not set.")

# # 🌐 Initialize Gemini API client
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # 🤖 Setup the model
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# # ⚙️ Configure run settings
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True,
# )

# # ➕ Tool to add two integers
# @function_tool
# def add(a: int, b: int) -> int:
#     """Add two integers."""
#     return a + b

# # ✖️ Tool to multiply two integers
# @function_tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two integers."""
#     return a * b

# # ➖ Tool to subtract two integers
# @function_tool
# def subtract(a: int, b: int) -> int:
#     """Subtract the second integer from the first."""
#     return a - b

# # ➗ Tool to divide two numbers
# @function_tool
# def divide(a: float, b: float) -> float:
#     """Divide the first number by the second number."""
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a / b

# # 🚀 Main function
# def main():
#     print("\n👋 Welcome to the **Math Tool Agent**! 🧮")
#     print("➕ I can help you with addition, subtraction, multiplication, and division.")
#     print("💬 Type a math question or type 'exit' to quit.\n")

#     agent = Agent(
#         name="MathToolBot",
#         instructions="🤖 You are a helpful math agent. Use the appropriate math tool when needed to solve problems. Only use the tools for calculations.",
#         model=model,
#         tools=[add, multiply, subtract, divide]
#     )

#     # Test the agent with three math questions
#     test_questions = [
#         "What is 15 plus 23?",
#         "Multiply 8 and 7 for me",
#         "If I have 100 apples and I give away 35, how many do I have left?"
#     ]
    
#     print("🧪 Testing the agent with some questions:\n")
#     for question in test_questions:
#         print(f"👤 Test Question: {question}")
#         result = Runner.run_sync(agent, question, run_config=config)
#         print(f"🤖 Bot: {result.final_output}\n")
    
#     print("✅ Testing complete! Now you can ask your own questions:\n")
    
#     while True:
#         user_input = input("\n👤 You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             print("👋 Goodbye! Have a great day! 🌟")
#             break

#         result = Runner.run_sync(agent, user_input, run_config=config)
#         print("🤖 Bot:", result.final_output)


# asyncio.run( main())   

import asyncio
from decouple import config
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig

gemini_api_key = config("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("🚨 GEMINI_API_KEY environment variable is not set.")

# 🌐 Initialize Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 🤖 Setup the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ⚙️ Configure run settings
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# ➕ Tool to add two integers
@function_tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

# ✖️ Tool to multiply two integers
@function_tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

# ➖ Tool to subtract two integers
@function_tool
def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first."""
    return a - b

# ➗ Tool to divide two numbers
@function_tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# 🚀 Main function
async def main():
    print("\n👋 Welcome to the **Math Tool Agent**! 🧮")
    print("➕ I can help you with addition, subtraction, multiplication, and division.")
    print("💬 Type a math question or type 'exit' to quit.\n")

    agent = Agent(
        name="MathToolBot",
        instructions="🤖 You are a helpful math agent. Use the appropriate math tool when needed to solve problems. Only use the tools for calculations.",
        model=model,
        tools=[add, multiply, subtract, divide]
    )

    # Test the agent with three math questions
    test_questions = [
        "What is 15 plus 23?",
        "Multiply 8 and 7 for me",
        "If I have 100 apples and I give away 35, how many do I have left?"
    ]
    
    print("🧪 Testing the agent with some questions:\n")
    for question in test_questions:
        print(f"👤 Test Question: {question}")
        result = await Runner.run(agent, question, run_config=config)
        print(f"🤖 Bot: {result.final_output}\n")
    
    print("✅ Testing complete! Now you can ask your own questions:\n")
    
    while True:
        user_input = input("\n👤 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye! Have a great day! 🌟")
            break

        result = await Runner.run(agent, user_input, run_config=config)
        print("🤖 Bot:", result.final_output)

asyncio.run(main())