from fastapi import APIRouter, Depends
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.llm_handler import FalconService

router = APIRouter()
falcon_service = FalconService()

@router.post("/chat")
async def chat_endpoint(
    message: str,
    current_user: User = Depends(get_current_active_user)
):
    try:
        response = await falcon_service.generate_text(message)
        return {
            "user": current_user.username,
            "message": message,
            "response": response,
            "model": "Falcon-7B"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Model error: {str(e)}"
        )