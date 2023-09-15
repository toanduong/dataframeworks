from insfrastructure.UnitOfWork import UnitOfWork
from Domains.Entities.Order import Order
class OrderHandler:
    def __init__(self):
        self.unitOfWork = UnitOfWork()
        self.orderEntity = self.unitOfWork.OrderEntity()

    def get(self):
        self.orderEntity.show(10)

    def add(self, order: Order):
        self.orderEntity.write.save("Orders", format="jdbc", mode="append", properties={**order})