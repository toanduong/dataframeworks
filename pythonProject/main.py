# This is a sample Python script.
import pyodbc
from pyarrow.util import guid

from Applications.OrderHandler import OrderHandler
from Configrutations.Configuration import IConfiguration
from Configrutations.SqlConfiguration import SqlConfiguration
from Domains.Entities.Order import Order
from Factories.DbContextFactory import DbContextFactory

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = Order(1, "2021-01-01", "Pending", 100.00, 1, 1)
    orderHandler = OrderHandler()
    orderHandler.add(order)

    #order = Order(1, "2021-01-01", "Pending", 100.00, 1, 1)
    #print(order)
    #print(order.LastModifiedDateUtc)

    #conn = dbconn.connect_to_sql()
    #conn.getinfo(pyodbc.SQL_DRIVER_NAME)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
