import os
import dotenv

dotenv.load_dotenv()


class Settings:

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
