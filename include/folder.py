from pathlib import Path

import shutil

class Folder:
    def __init__(self) -> None:
        self.__path: Path = Path("..") / "toppings"

    def recreate(self) -> None:
        if self.__path.exists():
            shutil.rmtree(self.__path)

        self.__path.mkdir()