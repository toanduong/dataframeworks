from pyspark import SparkConf, SparkContext
from insfrastructure.dbcontext import IDbcontext
from Configrutations.StorageConfiguration import StorageConfiguration

class StorageDbContext(IDbcontext):
    def __init__(self):
        self.config = StorageConfiguration().getConfig()

    def storageLocationURL(self, storageContainer: str, locationName: str) -> str:
        location = "abfss://" + storageContainer + "@" + self.config.storageAccount + ".dfs.core.windows.net/" + locationName + "/"
        return location

    def connect_to_sql(self):
        return SparkContext.getOrCreate()

    def connect(self):
        return self.connect_to_sql()