from fastapi import APIRouter, Depends, HTTPException
from app.models import User
from app.schemas import RegisterRequest, RegisterResponse
from app.db.session import GetDBSession, Session
from app.schemas.user import LoginRequest, LoginResponse
from app.utils import GenerateID, HashPassword, VerifyPassword

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
        hashed_password=HashPassword(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return RegisterResponse()


@router.post(
    "/login",
    status_code=200,
    response_model=LoginResponse,
)
async def LoginUser(
    request: LoginRequest,
    db: Session = Depends(GetDBSession),
) -> LoginResponse:

    user = db.query(User).filter(User.email == request.email).first()
    if not user or not VerifyPassword(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = "dummy_token"  # Replace with actual token generation logic

    return LoginResponse(token=token)
