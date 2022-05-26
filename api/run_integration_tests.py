from unittest import TestSuite
from unittest import TextTestRunner
from api.database.tests.mysqlconnector_test import MySQLConnectorIntegrationTestCase

def getMySQLConnectorIntegrationTestSuite():
    suite = TestSuite()

    todoItemTests = [ m for m in dir(MySQLConnectorIntegrationTestCase) if m.startswith('test_')]

    for test in todoItemTests:
        suite.addTest(MySQLConnectorIntegrationTestCase(test))

    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(getMySQLConnectorIntegrationTestSuite())
