from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List

from app.core.ai_agent import get_response_from_ai_agent

from app.config.settings import settings
from app.common.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title = "Multi-AI Agent")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str]
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request:RequestState):
    
