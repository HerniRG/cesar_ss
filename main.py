from simple_screen import Screen_manager
from app.controladores import CesarController

if __name__ == "__main__":
    with Screen_manager:
        cesar = CesarController()
        cesar.run()
