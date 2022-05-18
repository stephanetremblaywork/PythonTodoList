#!/usr/bin/python

class App():

    def __init__(self, ip_address="127.0.0.1", port=9000) -> None:
        self._ip_address = ip_address
        self._port = port

    def run(self) -> None:
        print("Hello world!")

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
