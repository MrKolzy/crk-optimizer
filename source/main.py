from include.window import Window

import sys

def main() -> int:
    window: Window = Window("BlueStacks App Player")
    if not window.maximize():
        return -1

    return 0

if __name__ == "__main__":
    sys.exit(main())