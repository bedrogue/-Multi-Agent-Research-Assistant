from pydantic import BaseModel

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    search_result: str
    scraped_content: str
    report: str
    feedback: str