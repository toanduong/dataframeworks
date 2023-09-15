from pyarrow.util import guid
from datetime import datetime

from Domains.Base.BaseEntity import BaseEntity
from dataclasses import dataclass, field
@dataclass
class Order(BaseEntity):
    OrderId: guid = field(init=False, default=guid())
    OrderNbr: int
    OrderDate: datetime
    OrderStatus: str
    Total: float
    CustomerId: guid
    Quantity: int
    TableName = "Orders"

    def updateTotal(self, total: float):
        self.Total = total
        return self