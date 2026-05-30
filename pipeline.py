from agents import build_agent_search,build_reader_agent,writer_chain,critic_chain

def run_search_agent(topic:str)->dict:
  state={}
  
  search_agent=build_agent_search()
  search_result=search_agent.invoke({
    "messages":[("user",f" Find recent,reliable and fetailed info about:{topic}")]
  })

  state["search_result"]=search_result["messages"][-1].content # kyuki create agent 4 output deta apn ko laast wala chahiye toh indexing
  print("\n search result ",state['search_result'])

  #-----------------------------------------------------------------------------------------------


  #calling second agent

  reader_agent=build_reader_agent()
  reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_result'][:800]}"
        )]
    })
  state['scraped_content'] = reader_result['messages'][-1].content
  print("\nscraped content: \n", state['scraped_content'])

  #----------------------------------------------------------------------------------------------


  #for writerchain we have to combine both result
  research_combined = (
        f"SEARCH RESULTS : \n {state['search_result']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

  
  state["report"]=writer_chain.invoke({
  "topic":topic,
  "research":research_combined
  })
  
  print("\n Final Report\n",state['report'])

  #------------------------------------------------------------------------------------------


  #cretic chain
  state["feedback"] = critic_chain.invoke({
        "report":state['report']
    })

  print("\n critic report \n", state['feedback'])

  return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_search_agent(topic)

