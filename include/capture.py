from pathlib import Path

import pyautogui as pag

class Capture:
    def __init__(self, path: Path) -> None:
        self.__path : Path = path
        self.__index: int  = 1

    def __capture(self):
        capture = pag.screenshot()
        capture.save(self.__path / f"topping_{self.__index}.png")
        self.__index += 1