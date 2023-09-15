from pydantic import BaseModel
from typing import Optional

class StorageConfigModel(BaseModel):
    name: Optional[str] = None
    key: Optional[str] = None
    container: Optional[str] = None