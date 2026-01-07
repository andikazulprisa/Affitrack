import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/affitrack"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY", "affitrack_secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "affitrack_jwt_secret_key")