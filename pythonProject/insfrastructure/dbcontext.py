from pyspark.sql import SparkSession, DataFrame
from abc import ABC, abstractmethod
from Configrutations.SqlConfiguration import SqlConfiguration

class IDbcontext(ABC):
    @abstractmethod
    def connect(self):
        pass

class SqlDbcontext(IDbcontext):
    def __init__(self):
        self.config = SqlConfiguration().getConfig()
        self.connectionString = f"jdbc:sqlserver://{self.config.server};databaseName={self.config.database};user={self.config.username};password={self.config.password}"

    def connect(self):
        spark = SparkSession.builder \
            .appName("dataframework") \
            .getOrCreate()

        self.spark = spark
        return self

    def get(selfs, table: str) -> DataFrame:
        return selfs.spark.read \
            .format("jdbc") \
            .option("url", selfs.connectionString) \
            .option("dbtable", table) \
            .load()

    def add(selfs, table: str) -> DataFrame:
        return selfs.spark.read \
            .format("jdbc") \
            .option("url", selfs.connectionString) \
            .option("dbtable", table) \
            .load()

