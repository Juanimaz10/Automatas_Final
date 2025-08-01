from main import MainMenu
from constant import USER_INPUT_OPTION_TO_MAIN_MENU

class User:
    def __init__(self) -> None:
        optionMainMenuToUserChoice = int(input(USER_INPUT_OPTION_TO_MAIN_MENU))
        self.__mainMenu = MainMenu(optionMainMenuToUserChoice)


    @property
    def MainMenuWithOptionSelectedByTheUser(self):
        return self.__mainMenu