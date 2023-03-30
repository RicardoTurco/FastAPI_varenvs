from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Application general settings class, which inherits from 'BaseSettings' from pydantic.
    """

    # Groups
    VAR_AMB_G1: str
    VAR_AMB_G2: str
    VAR_AMB_G3: str

    # Users
    VAR_AMB_U1: str
    VAR_AMB_U2: str
    VAR_AMB_U3: str

    class Config:
        """
        Configurations of pydantic ...
        """
        env_file = ".env"
