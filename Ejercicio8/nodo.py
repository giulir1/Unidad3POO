class Nodo:
    __personal = None
    __siguiente = None

    def __init__(self, personal):
        self.__personal = personal
        self.__siguiente = None

    def setSiguiente(self, personal):
        self.__siguiente = personal

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__personal
