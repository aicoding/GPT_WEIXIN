from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,AIMessage,ChatMessage
from langchain.tools import format_tool_to_openai_function,YouTubeSearchTool,MoveFileTool

llm = ChatOpenAI(model="")
tools = [MoveFileTool()]
functions = [format_tool_to_openai_function(t) for t in tools]

message = llm.predict_messages([HumanMessage(content='move file foo to bar'),functions])



