from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app import models, schemas, utils
from app.database import get_db
import uuid

router = APIRouter()

@router.post("/register", status_code=201)
async def register(user: schemas.UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")
    hashed = utils.hash_password(user.password)
    confirmation_token = str(uuid.uuid4())
    db_user = models.User(
        email=user.email,
        hashed_password=hashed,
        is_confirmed=False,
        confirmation_token=confirmation_token
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # Simulate async email sending
    background_tasks.add_task(utils.send_confirmation_email, user.email, confirmation_token)
    return {"msg": "User registered. Please check your email to confirm."}

@router.post("/confirm", status_code=200)
def confirm_email(req: schemas.EmailConfirm, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(email=req.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    if user.is_confirmed:
        return {"msg": "Email already confirmed."}
    if user.confirmation_token != req.token:
        raise HTTPException(status_code=400, detail="Invalid confirmation token.")
    user.is_confirmed = True
    user.confirmation_token = None
    db.commit()
    return {"msg": "Email confirmed. You may now log in."}

@router.post("/login", response_model=schemas.Token)
def login(login_req: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(email=login_req.email).first()
    if not user or not utils.verify_password(login_req.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    if not user.is_confirmed:
        raise HTTPException(status_code=403, detail="Email not confirmed.")
    token = utils.create_jwt(user.email)
    return {"access_token": token, "token_type": "bearer"}
