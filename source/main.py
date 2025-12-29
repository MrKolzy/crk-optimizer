from include.capture import Capture
from include.folder  import Folder
from include.window  import Window

import sys

ROWS: int = 8

def main() -> int:
    window: Window = Window("BlueStacks App Player")
    if not window.maximize():
        return -1

    folder: Folder = Folder()
    folder.recreate()

    capture: Capture = Capture(ROWS)

    return 0

if __name__ == "__main__":
    sys.exit(main())