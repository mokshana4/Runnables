from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage

from rich import print

#creating a tool

@tool
def get_text_length(text : str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}

llm = ChatMistralAI(model = "mistral-small-latest")
#toolbinding
llm_with_tool = llm.bind_tools([get_text_length])

#STEP-1 llm decides tool
# result = llm_with_tool.invoke(
#     "Use the get_text_length tool to find the length of: hello how are you"
# )

# #STEP-2:4 Execute tool
# if result.tool_calls:
#     tool_call = result.tool_calls[0]
#     tool_result = get_text_length.invoke(tool_call["args"])

#     #STEP-5 Send back to llm
#     final_response = llm.invoke(
#         f"The length of the text is {tool_result}"
#     )

#     print(final_response)

message = []
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

if result.tool_calls:   
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)
    print(message)

result = llm_with_tool.invoke(message)
print(result.content)