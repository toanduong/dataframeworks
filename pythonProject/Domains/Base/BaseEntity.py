from datetime import date
from dataclasses import dataclass, field

@dataclass(slots=True)
class BaseEntity:
    IsEnabled: bool = field(init=False, default=True, repr=False)
    CreatedDateUtc: date = field(init=False, default=date.today(), repr=False)
    LastModifiedDateUtc: date = field(init=False, default=date.today(), repr=False)
    TableName: str = field(init=False, default="", repr=False)
