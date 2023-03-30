from fastapi import APIRouter, Response, status
from app.extension.general_constants import ConstUsers


router = APIRouter()

tag = "Users"


@router.get("/vars", tags=[tag], summary="Get vars of user")
def get_vars_of_user(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"user_var1": ConstUsers.VAR_AMB_U1,
            "user_var2": ConstUsers.VAR_AMB_U2,
            "user_var3": ConstUsers.VAR_AMB_U3}
