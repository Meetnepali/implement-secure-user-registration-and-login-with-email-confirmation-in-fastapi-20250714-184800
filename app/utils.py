from passlib.context import CryptContext
import time
import jwt
from typing import Any

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = "TEST_SECRET_CHANGE_IN_PROD"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_SECONDS = 3600

# Minimal password hashing/validation interface
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_jwt(email: str) -> str:
    payload = {
        "sub": email,
        "exp": int(time.time()) + JWT_EXPIRATION_SECONDS
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def send_confirmation_email(email: str, token: str):
    # Simulate sending (would send email in prod)
    print(f"SIMULATED EMAIL to {email}: Your confirmation token is {token}")
