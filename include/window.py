import pyautogui as pag
import win32con
import win32gui

class Window:
    def __init__(self, name: str) -> None:
        self.__name  : str = name
        self.__handle: int = win32gui.FindWindow(None, name)

    def maximize(self) -> bool:
        if not self.__handle:
            print("[Error]: The window could not be found")
            return False

        # Restore if minimized
        if win32gui.IsIconic(self.__handle):
            win32gui.ShowWindow(self.__handle, win32con.SW_RESTORE)

        # Bring to the foreground if it's not already there
        if self.__handle != win32gui.GetForegroundWindow():
            win32gui.SetForegroundWindow(self.__handle)

        # Switch BlueStacks to fullscreen mode
        left, top, right, bottom = win32gui.GetWindowRect(self.__handle)
        height = bottom - top
        if height != 1080:
            pag.press("F11")

        return True