from pydantic_settings import BaseSettings


class Conf(BaseSettings):
    pg_user: str
    pg_db: str
    pg_pass: str
    pg_host: str = "localhost"
    pg_port: int

    secret_key: str
    wtf_scrf_secret_key: str

    @property
    def db_uri(self):
        return f"postgresql://{self.pg_user}:{self.pg_pass}@{self.pg_host}:{self.pg_port}/{self.pg_db}"


conf = Conf()
