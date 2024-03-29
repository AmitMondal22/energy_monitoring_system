
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from config.JWT_config import SECRET_KEY,ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    try:
        to_encode = data.copy()
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": (datetime.utcnow() + access_token_expires).isoformat()})
        print("Access token data:", to_encode)
        encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except JWTError as e:
        # Handle JWT encoding errors
        print("JWT encoding error:", e)
        return None