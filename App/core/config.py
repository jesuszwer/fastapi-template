from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict, TomlConfigSettingsSource


class ApplicationConfig(BaseModel):
    host: str
    name: str
    port: int
    reload: bool


class ApiConfig(BaseModel):
    version: int = 1
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    echo: bool
    url: PostgresDsn

    naming_conventions: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    app: ApplicationConfig
    api: ApiConfig = ApiConfig()
    db: DatabaseConfig

    model_config = SettingsConfigDict(
        toml_file="dev.toml",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (TomlConfigSettingsSource(settings_cls, "dev.toml"),)


settings = Settings()
