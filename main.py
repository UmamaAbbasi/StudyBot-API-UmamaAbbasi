from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file")
app = FastAPI(title="Study Bot API")
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)
class ChatRequest(BaseModel):
    user_input: str
@app.get("/")
def home():
    return {"message": "Study Bot is running successfully 🚀"}
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        messages = [
            SystemMessage(content="""
You are StudyBot, an AI academic assistant.
Explain answers clearly.
Give step-by-step explanations.
Keep answers simple and student-friendly.
"""),
            HumanMessage(content=request.user_input)
        ]
        response = await llm.ainvoke(messages)

        return {
            "user_question": request.user_input,
            "bot_response": response.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))