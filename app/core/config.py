import os
from dotenv import load_dotenv

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin.auth import verify_id_token

load_dotenv()

bearer_scheme = HTTPBearer(auto_error=False)
def get_firebase_user_from_token(
    token: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
) -> dict | None:
    """Uses bearer token to identify firebase user id
    Args:
        token : the bearer token. Can be None as we set auto_error to False
    Returns:
        dict: the firebase user on success
    Raises:
        HTTPException 401 if user does not exist or token is invalid
    """
    try:
        if not token:
            # raise and catch to return 401, only needed because fastapi returns 403
            # by default instead of 401 so we set auto_error to False
            raise ValueError("No token")
        user = verify_id_token(token.credentials)
        return user
    # lots of possible exceptions, see firebase_admin.auth,
    # but most of the time it is a credentials issue
    except Exception:
        # we also set the header
        # see https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in or Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set")

if not DB_NAME:
    raise ValueError("DB_NAME is not set")

if not os.path.exists("service-account.json"):
    raise ValueError("service-account.json is not found")
