from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from loguru import logger
from typing_extensions import TypedDict

from src.tools import calculate_budget, search_flights, search_hotels

# Configure logger
logger.remove()  # Remove default handler
logger.add("agent.log", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}", level="DEBUG")
logger.add(lambda msg: print(msg, end=""), format="{message}", level="INFO")  # Also print to console

load_dotenv()


# 1. Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# 2. Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)


# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)

    # LOGGING
    if response.tool_calls:
        logger.info(f"LLM triggered {len(response.tool_calls)} tool call(s)")
        for tc in response.tool_calls:
            logger.info(f"  → Tool: {tc['name']}, Arguments: {tc['args']}")
    else:
        logger.info("Direct LLM response (no tools used)")

    return {"messages": [response]}


# 5 Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)
# TODO: Sinh viên khai báo báo edge
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()

# 6. Chat loop
if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("TravelBuddy - Trợ lý Du lịch Thông minh")
    logger.info("Type 'quit', 'exit', or 'q' to exit.")
    logger.info("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            logger.info("User exiting chat loop.")
            break

        logger.info(f"Processing user query: {user_input}")
        try:
            result = graph.invoke({"messages": [{"type": "human", "content": user_input}]})
            final = result["messages"][-1]
            logger.info(f"Generated response: {final.content[:100]}...")
            print(f"\nTravelBuddy: {final.content}")
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}", exc_info=True)
            print(f"❌ Error: {str(e)}")
