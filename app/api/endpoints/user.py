from fastapi import APIRouter

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)
users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
for route in users_router.routes:
    if 'DELETE' in route.methods:
        users_router.routes.remove(route)
        break
router.include_router(
    users_router,
    prefix='/users',
    tags=['users']
)
