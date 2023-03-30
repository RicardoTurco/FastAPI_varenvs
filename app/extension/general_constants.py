from functools import lru_cache
from config import Settings


@lru_cache()
def get_settings():
    return Settings()


# Returning all environment variables ...
settings = get_settings()


"""
SEPARATING the environment variables ... 
"""


class ConstGroups:

    VAR_AMB_G1 = settings.VAR_AMB_G1
    VAR_AMB_G2 = settings.VAR_AMB_G2
    VAR_AMB_G3 = settings.VAR_AMB_G3


class ConstUsers:

    VAR_AMB_U1 = settings.VAR_AMB_U1
    VAR_AMB_U2 = settings.VAR_AMB_U2
    VAR_AMB_U3 = settings.VAR_AMB_U3
