class Pizza:
    def __init__(self):
        self.__crusts: list[str] = []
        self.__sauces: list[str] = []
        self.__toppings: list[str] = []
        self.__cheeses: list[str] = []
        # TODO: Future Additions

    def __str__(self):
        return f"""
        Crusts: {self.__crusts}\n
        Sauces: {self.__sauces}\n
        Toppings: {self.__toppings}\n
        Cheese: {self.__cheese}\n
        """

    @property
    def get_crusts(self) -> list[str]:
        return self.__crusts

    @get_crusts.setter
    def set_crusts(self, crusts: list, expand: bool = True):
        if expand and self.getCrusts() != []:
            self.__crusts.extend(crusts)
        else:
            self.__crusts = crusts

    @property
    def get_sauces(self) -> list[str]:
        return self.__sauces

    @get_sauces.setter
    def set_sauces(self, sauces: list, expand: bool = True):
        if expand and self.getSauces() != []:
            self.__sauces.extend(sauces)
        else:
            self.__sauces = sauces

    @property
    def get_toppings(self) -> list[str]:
        return self.__toppings

    @get_toppings.setter
    def set_toppings(self, toppings: list, expand: bool = True):
        if expand and self.getToppings() != []:
            self.__toppings.extend(toppings)
        else:
            self.__toppings = toppings

    @property
    def get_cheeses(self) -> list[str]:
        return self.__cheese

    @get_cheeses.setter
    def set_cheeses(self, cheese: list, expand: bool = True):
        if expand and self.getCheeses() != []:
            self.__cheese.extend(cheese)
        else:
            self.__cheese = cheese
        self.__cheese = cheese
