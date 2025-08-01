from constant import MAIN_MENU
from sqlalchemy.ext.hybrid import hybrid_property


class MainMenu:
    def __init__(self, optionByUserSelect:int) -> None:
        self.__option = optionByUserSelect

    @hybrid_property
    def option(self) -> int:
        return self.__option
    @option.setter
    def option(self, optionChoosedByUser) -> None:
        self.__option = optionChoosedByUser


    @staticmethod
    def show():
        return MAIN_MENU