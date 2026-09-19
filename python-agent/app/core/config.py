from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "CRM Lead Qualifier Agent"
    environment: str = "dev"
    database_url: str = "sqlite+aiosqlite:///./leads.db"
    crm_base_url: str = "http://java-crm-service:8080"
    openai_api_key: str | None = None
    llm_model: str = "gpt-4o-mini"
    max_agent_steps: int = 8
    qualification_threshold: int = 70
    review_threshold: int = 45
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
settings = Settings()
