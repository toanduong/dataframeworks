from Factories.DbContextFactory import DbContextFactory

class UnitOfWork:
    def __init__(self):
        self.dbFactory = DbContextFactory()
        self.sqlDbContext = self.dbFactory.SQL()

    def OrderEntity(self):
        return self.sqlDbContext.connect().get("Orders")