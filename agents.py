from langchain.agents import create_agent # import create agent
from langchain_groq import ChatGroq #import llm
from langchain_core.prompts import ChatPromptTemplate # PROMPT CREATE KRNA HOGA
from langchain_core.output_parsers import StrOutputParser # STRUCTURE OUTPUT KE LIYE
from tool1 import web_search,scrape_url # our tool exporting
from dotenv import load_dotenv
import os


llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0) # using llm model 

# creating agent
def build_agent_search():
    return create_agent (
        model=llm,
        tools=[web_search]
    )

#2nd agent 

def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

# now we create two chain writer chain prompy-> llm -> structture output  using lcel piple
#cretic chain which gives report to feedback using lcel pipline

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()
#-----------------------------------------------------------------------------------------------------



critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()


