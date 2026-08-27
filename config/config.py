from pydantic_settings import BaseSettings

class Conf(BaseSettings):
    pg_user: str
    pg_db: str
    pg_pass: str
    pg_host: str = "localhost"

    secret_key: str
    wtf_scrf_secret_key: str


conf = Conf()

