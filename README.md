
# Hospital Recommendation System

This is an AI-powered hospital recommendation system built with LangChain, Google Gemini (LLM), and FastAPI.
It intelligently recommends the most suitable hospital department based on a patient's gender, age, and reported symptoms.

Features:
1. AI-driven diagnosis support — determines the most appropriate medical department (e.g., Cardiology, Neurology, Orthopedics, etc.) based on patient data.
2. Uses LangChain to structure prompts and manage interactions with the Gemini LLM.
3. Powered by Google Gemini (langchain-google-genai) to perform contextual medical reasoning.
4. Environment-secured API keys using .env and python-dotenv.
5. FastAPI backend for scalable and high-performance REST endpoints.

Backend Framework: FastAPI
LLM Framework: LangChain
Language Model: Google Gemini (Gemini 2.5 Flash)
Environment Management: python-dotenv
Runtime: Python 3.13.2


## Installation

1. Clone the repository:

git clone https://github.com/Ninissdyah/hospital-ai.git

2. Create a Virtual Environment:

python -m venv venv
venv\Scripts\activate (activate the Environment for windows)

3. Install Dependencies:

pip install -r requirements.txt

4. Create a file named .env in the project root directory and add your Google Gemini API key:

GOOGLE_API_KEY=your_google_ai_studio_api_key_here

5. Run the FastAPI Server:

cd venv
uvicorn app.main:app --reload

6. Test the API:

open your browser and visit the link: http://127.0.0.1:8000/docs
OR
run in another terminal: python app/test.py




    