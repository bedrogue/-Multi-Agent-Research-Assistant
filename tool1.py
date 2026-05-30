import warnings
warnings.filterwarnings("ignore")
from langchain.tools import tool
import requests # taaol h yeh
from bs4 import BeautifulSoup  # toool h hai
from tavily import TavilyClient # tavily tool
import os

from dotenv import load_dotenv # env file ko import krwane ke 
load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
#



# tavilyy toool h yehhh 
@tool
def web_search(query:str)->str:
    """search the web result for the query and return the result"""
    result=tavily.search(query=query,max_results=5)
    return result
# yeh tavily bot search kr rha h 
    out=[]   
    for r in result["results"]:
        out.append(
              f"Title:{r["title"]}\nURL:{r["url"]}\nSnippet:{r["content"][:300]}\n"
        )
    return"\n\n".join(out)
#print(web_search.invoke("who is the prime minsiter of india"))
############################################################################################################
# tavilyy toool tha yeh 
# ab isko conect krna h  

@tool 
def scrape_url(url:str)->str:
    "scrape tool clean content dega jo usne wensite se scrape kiya h"
    try:
        res=requests.get(url,timeout=8,headers={"User-agent":"Mozilla/5.0"})
        soup=BeautifulSoup(res.text,"html.parser")
        for tag in soup(["scipt","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"could not scrape URL:{str(e)}"
    
#print(scrape_url.invoke("https://www.ucpress.edu/blog-posts/an-exploration-into-indias-adult-film-industry"))


