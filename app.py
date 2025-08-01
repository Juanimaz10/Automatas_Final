from main import MainMenu
from user import User
from main_controller import MainMenuController


class App:

    def start(self):
        mainMenu = MainMenu(...)
        while mainMenu.option != 8:
            print(MainMenu.show())
            user = User()
            mainMenuController = MainMenuController(user.MainMenuWithOptionSelectedByTheUser)
            mainMenuController.runTheServiceThatTheUserChose()


if __name__ == '__main__':
    app = App()
    app.start()