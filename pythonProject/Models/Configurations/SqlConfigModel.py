from pydantic import BaseModel
from typing import Optional

class SqlConfigModel(BaseModel):
    driver: Optional[str] = None
    server: Optional[str] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
