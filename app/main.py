from fastapi import FastAPI
from .models import inputData
from .services import get_recommendation

app = FastAPI(
    title="Hospital Recommendation System"
)

@app.post("/recommend")
async def recommend_department(data: inputData):
    try:
        department = get_recommendation(data)
        return {"recommended_department": department}
    except Exception as e:
        return {"recommended_department": f"error: {str(e)}"}
