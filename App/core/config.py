from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict, TomlConfigSettingsSource


class ApplicationConfig(BaseModel):
    host: str
    name: str
    port: int
    reload: bool


class DatabaseConfig(BaseModel):
    echo: bool
    url: PostgresDsn


class Settings(BaseSettings):
    app: ApplicationConfig
    db: DatabaseConfig

    model_config = SettingsConfigDict(
        toml_file="dev.toml",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (TomlConfigSettingsSource(settings_cls, "dev.toml"),)


settings = Settings()
