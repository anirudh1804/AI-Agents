from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
load_dotenv()

web_agent = Agent(
    name = "Web-Agent-Ducky",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources of information"],
    show_tool_calls = True,
    markdown = True
)

finance_agent = Agent(
    name = "Finance-Agent-Krabby",
    role = "Retrieve financial information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls = True,
    markdown=True,
    instructions=["Use tables to display data"],
    debug_mode = False
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions = ["Always include sources of information", "Use tables to display data"],
    show_tool_calls = True,
    markdown = True
)

agent_team.print_response("What is the overall financial status Apple company recently?",
                          stream=True)