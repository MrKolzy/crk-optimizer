from include.capture import Capture
from include.folder  import Folder
from include.window  import Window

import sys

FOLDER_NAME: str = "toppings"

def main() -> int:
    window: Window = Window("BlueStacks App Player")
    if not window.maximize():
        return -1

    folder: Folder = Folder(FOLDER_NAME)
    folder.recreate()

    capture: Capture = Capture(folder.get_path())

    return 0

if __name__ == "__main__":
    sys.exit(main())