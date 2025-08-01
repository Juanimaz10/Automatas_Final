from constant import PROGRAM_OFF
from main import MainMenu
from sys import exit
from option_1 import Option1
from option_2 import Option2
from option_3 import Option3
from option_4 import Option4
from option_5 import Option5
from option_6 import Option6
 

class MainMenuController:
    def __init__(self, mainMenu:MainMenu) -> None:
        self.__mainMenuOptionChosenByTheUser = mainMenu.option
        self.__serviceChoosedByMainMenuOption = {1: Option1,
                                                 2: Option2,
                                                 3: Option3,
                                                 4: Option4,
                                                 5: Option5,
                                                 6: Option6,
                                                 7: ...}


    def runTheServiceThatTheUserChose(self):
        if 6 >= self.__mainMenuOptionChosenByTheUser >= 1:
            return self.__serviceChoosedByMainMenuOption[self.__mainMenuOptionChosenByTheUser].execute()
        exit(PROGRAM_OFF)