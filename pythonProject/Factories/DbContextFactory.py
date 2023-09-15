from abc import ABC, abstractmethod
from insfrastructure.dbcontext import SqlDbcontext

class IDbContextFactory(ABC):
    @abstractmethod
    def SQL(self) -> SqlDbcontext:
        pass

class DbContextFactory(IDbContextFactory):
    def SQL(self) -> SqlDbcontext:
        return SqlDbcontext()