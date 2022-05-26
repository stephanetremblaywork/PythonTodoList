
class ConnectionProperties():
    def __init__(self, host, port, dbName, user, password):
        self._host = host
        self._port = port
        self._dbName = dbName
        self._user = user
        self._password = password

    def getHost(self) -> str:
        return self._host
    
    def getPort(self) -> int:
        return self._port
    
    def getDbName(self) -> str:
        return self._dbName

    def getUser(self) -> str:
        return self._user
    
    def getPassword(self) -> str:
        return self._password