from fastapi import APIRouter
from app.controller import group, user


router = APIRouter()


router.include_router(group.router, prefix="/groups",)
router.include_router(user.router, prefix="/users",)
