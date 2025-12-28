from pathlib import Path

import shutil

class Folder:
    def __init__(self, name: str) -> None:
        self.__name: str  = name
        self.__path: Path = Path("..") / self.__name

    def recreate(self) -> None:
        if self.__path.exists():
            shutil.rmtree(self.__path)

        self.__path.mkdir()

    def get_path(self) -> Path:
        return self.__path