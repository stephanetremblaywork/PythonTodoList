from unittest import TestSuite
from unittest import TextTestRunner
from api.database.tests.mysqlconnector_test import MySQLConnectorTestCase
from api.database.tests.mysqlconnector_test import MySQLConnectorIntegrationTestCase

def getMySQLConnectorTestSuite():
    suite = TestSuite()

    todoItemTests = [ m for m in dir(MySQLConnectorTestCase) if m.startswith('test_')]

    for test in todoItemTests:
        suite.addTest(MySQLConnectorTestCase(test))

    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(getMySQLConnectorTestSuite())
