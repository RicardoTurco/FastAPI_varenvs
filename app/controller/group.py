from fastapi import APIRouter, Response, status
from app.extension.general_constants import ConstGroups


router = APIRouter()

tag = "Groups"


@router.get("/vars", tags=[tag], summary="Get vars of group")
def get_vars_of_group(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"group_var1": ConstGroups.VAR_AMB_G1,
            "group_var2": ConstGroups.VAR_AMB_G2,
            "group_var3": ConstGroups.VAR_AMB_G3}
