from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, Tool
import json
from typing import List
import dotenv

dotenv.load_dotenv()

app = FastAPI(title="Loan Risk Assessment Agent")


@Tool
def market_analysis(product: str) -> int:
    '''
    Perform market analysis of a product to assess loan risk.
    '''
    pass

@Tool
def tool2():
    pass


@Tool
def sentiment_analysis(feedbacks: List[str]) -> int:
    '''
    Perform sentiment analysis on the feedbacks on the products sold by artisan to assess loan risk.
    '''
    pass



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

tools = []

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)