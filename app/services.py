import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY tidak ditemukan di file .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.0,
    google_api_key=api_key
)

prompt = ChatPromptTemplate.from_template("""
You are a hospital triage system.
Based on the following patient data:

Gender: {gender}
Age: {age}
Symptoms: {symptoms}

Determine the most appropriate specialty department 
(e.g., Neurology, Cardiology, Orthopedics, etc.).
Answer with the department name only.
""")

parser = StrOutputParser() #parser pngganti LLM.chain

chain = prompt | llm | parser #pipeline baru prompt>LLM>parser

def get_recommendation(data):

    response = chain.invoke({
        "gender": data.gender,
        "age": data.age,
        "symptoms": " ,".join(data.symptoms)
    })
    return response.strip()
