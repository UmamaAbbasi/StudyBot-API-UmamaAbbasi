# 📚 StudyBot – AI Academic Assistant

StudyBot is an AI-powered academic assistant built using FastAPI and Groq LLM.  
It provides clear, step-by-step explanations and supports conversational memory using MongoDB.

## 🚀 Features

- AI-powered responses using Groq LLM
- Step-by-step explanations
- Context-aware conversation
- MongoDB-based memory storage
- RESTful API architecture
- Swagger API documentation

## 🛠 Technologies Used

- Python
- FastAPI
- LangChain
- Groq API (llama-3.1-8b-instant)
- MongoDB
- Uvicorn

## 📦 Installation (Run Locally)

1️⃣ Clone the Repository
git clone https://github.com/UmamaAbbasi/StudyBot-API-UmamaAbbasi.git
cd studybot-api
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Create .env File

Create a .env file and add:

GROQ_API_KEY=your_actual_key
MONGO_URI=your_mongodb_connection_string
4️⃣ Run the Server
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/docs
📌 API Endpoint
POST /chat
Request:
{
  "user_input": "Explain Newton's First Law"
}
Response:
{
  "user_question": "Explain Newton's First Law",
  "bot_response": "Step-by-step explanation..."
}
