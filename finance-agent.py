from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent = Agent(
    model = Groq(id="openai/gpt-oss-120b"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls = True,
    markdown=True,
    instructions=["Use tables to display data"],
    debug_mode = True
)

agent.print_response("Summarize and compare stock fundamentals information and stock prices of Apple and Samsung in the last 5 years")