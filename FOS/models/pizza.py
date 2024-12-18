class Pizza:
    def __init__(self):
        self.__crusts: list[str] = []
        self.__sauces: list[str] = []
        self.__toppings: list[str] = []
        self.__cheese: list[str] = []
        # TODO: Future Additions

    def __str__(self):
        return f"""
        Crusts: {self.__crusts}\n
        Sauces: {self.__sauces}\n
        Toppings: {self.__toppings}\n
        Cheese: {self.__cheese}\n
        """

    @property
    def getCrusts(self) -> list[str]:
        return self.__crusts

    @getCrusts.setter
    def setCrusts(self, crusts: list, expand: bool = True):
        if expand and self.getCrusts() != []:
            self.__crusts.extend(crusts)
        else:
            self.__crusts = crusts

    @property
    def getSauces(self) -> list[str]:
        return self.__sauces

    @getSauces.setter
    def setSauces(self, sauces: list, expand: bool = True):
        if expand and self.getSauces() != []:
            self.__sauces.extend(sauces)
        else:
            self.__sauces = sauces

    @property
    def getToppings(self) -> list[str]:
        return self.__toppings

    @getToppings.setter
    def setToppings(self, toppings: list, expand: bool = True):
        if expand and self.getToppings() != []:
            self.__toppings.extend(toppings)
        else:
            self.__toppings = toppings

    @property
    def getCheeses(self) -> list[str]:
        return self.__cheese

    @getCheeses.setter
    def setCheeses(self, cheese: list, expand: bool = True):
        if expand and self.getCheeses() != []:
            self.__cheese.extend(cheese)
        else:
            self.__cheese = cheese
        self.__cheese = cheese
