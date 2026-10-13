from google.adk.agents import Agent
from .prompt import Instructions,cust_prompt
from .tools.calculator_tool import addition,Subtraction,multiplication,divide,calculate
from .tools.customer_tools import get_customer_details,get_account_transactions
from .tools.Account_tool import get_account_details
from .tools.retrieve_tool import search_knowledge_base
from google.adk.agents.llm_agent import LlmAgent

root_agent = Agent(
    name="banking_customer_support_agent",
    model="gemini-3.6-flash",
    description="you are helpful banking support agent",
    instruction=cust_prompt,
    tools=[get_customer_details,get_account_details,search_knowledge_base]
)
