import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Change this to a long random string before deploying!
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-to-a-random-secret-key")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'portfolio.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER_PROJECTS = os.path.join(BASE_DIR, "static", "uploads", "projects")
    UPLOAD_FOLDER_PROFILE = os.path.join(BASE_DIR, "static", "uploads", "profile")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp", "svg"}
    MAX_CONTENT_LENGTH = 6 * 1024 * 1024  # 6 MB upload limit
