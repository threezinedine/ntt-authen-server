from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import RegisterRequest, RegisterResponse
from app.db.session import GetDBSession, Session
from app.services import GenerateID

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=201,
)
async def RegisterUser(
    request: RegisterRequest,
    db: Session = Depends(GetDBSession),
) -> RegisterResponse:
    user = User(
        id=GenerateID(),
        email=request.email,
        hashed_password=request.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return RegisterResponse()
