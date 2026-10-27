from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the agent with an LLM via Groq and DuckDuckGoTools
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],      # Add DuckDuckGo tool to search the web
    show_tool_calls=True,           # Shows tool calls in the response, set to False to hide
    markdown=True                   # Format responses in markdown
)

# Prompt the agent to fetch a breaking news story from New York
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
python3 -m venv .venv
source .venv/bin/activate
pip install -U groq agno duckduckgo-search
GROQ_API_KEY="your-api-key"
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
python web_search_agent.py
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),  # You can use a different model for the team leader agent
    instructions=["Always include sources", "Use tables to display data"],
    # show_tool_calls=True,  # Uncomment to see tool calls in the response
    markdown=True,
)

# Give the team a task
agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
