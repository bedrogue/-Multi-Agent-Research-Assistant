from fastapi import FastAPI, HTTPException
from schema import ResearchRequest, ResearchResponse
from pipeline import run_search_agent

app = FastAPI(
    title="Multi-Agent Research API",
    description="AI-powered research using LangGraph + Groq",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "running", "message": "Multi-Agent Research API"}

@app.post("/research", response_model=ResearchResponse)
def research(req: ResearchRequest):
    if not req.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    
    try:
        state = run_search_agent(req.topic)
        return ResearchResponse(
            search_result=state.get("search_result", ""),
            scraped_content=state.get("scraped_content", ""),
            report=state.get("report", ""),
            feedback=state.get("feedback", "")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))