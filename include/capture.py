from pathlib import Path

import pyautogui as pag
import time

class Capture:
    def __init__(self, rows: int) -> None:
        self.__path : Path = Path("..") / "toppings"
        self.__index: int  = 1
        self.__rows : int  = rows

    def __capture(self) -> None:
        capture = pag.screenshot()
        capture.save(self.__path / f"topping_{self.__index}.png")
        self.__index += 1

    def __select_topping(self, number: int) -> None:
        # Coordinates of the first topping
        topping_x: int = 1086
        topping_y: int = 331

        # Algorithm variables
        row_number  : int = 0
        block_number: int = 1
        counter     : int = 1

        # Vertical loop
        for j in range(1, self.__rows + 1):
            # Scroll four rows if more than four remain
            if (j - 1) % 4 == 0 and self.__rows - j >= 3 and j > 4:
                pag.click(1086, 331 + (80 + 12 + 80) * 3)
                pag.mouseDown()
                pag.moveTo(1086, 305, duration = 1)
                time.sleep(0.6)
                pag.mouseUp()

                # Move to the first topping
                topping_x = 1086
                topping_y = 331

            #Scroll one row if fewer than four remain
            elif self.__rows < block_number * 4 and j >= 4:
                pag.click(1086, 331 + (80 + 12 + 80) * 3)
                pag.mouseDown()
                pag.moveTo(1086, 666, duration = 1)
                time.sleep(0.6)
                pag.mouseUp()

                # Move to the first column and the fourth row
                topping_x = 1086
                topping_y = 331 + (80 + 12 + 80) * 3

            # Horizontal loop
            for i in range(1, 6):
                if counter == number:
                    pag.click(topping_x, topping_y)
                    return

                # Each topping is 160x160 px, with 12 px spacing
                topping_x += 80 + 12 + 80
                counter   += 1

            # Move to the first column and the next row
            topping_x  = 1086
            topping_y += 80 + 12 + 80

            # Algorithm calculations
            row_number += 1
            if row_number % 4 == 0:
                block_number += 1

    def __iterate_all(self) -> None:
        # Coordinates of the first topping
        topping_x: int = 1086
        topping_y: int = 331

        # Algorithm variables
        row_number  : int = 0
        block_number: int = 1
        counter     : int = 1

        # Vertical loop
        for j in range(1, self.__rows + 1):
            # Scroll four rows if more than four remain
            if (j - 1) % 4 == 0 and self.__rows - j >= 3 and j > 4:
                pag.click(1086, 331 + (80 + 12 + 80) * 3)
                pag.mouseDown()
                pag.moveTo(1086, 305, duration = 1)
                time.sleep(0.6)
                pag.mouseUp()

                # Move to the first topping
                topping_x = 1086
                topping_y = 331

            # Scroll one row if fewer than four remain
            elif self.__rows < block_number * 4 and j >= 4:
                pag.click(1086, 331 + (80 + 12 + 80) * 3)
                pag.mouseDown()
                pag.moveTo(1086, 666, duration = 1)
                time.sleep(0.6)
                pag.mouseUp()

                # Move to the first column and the fourth row
                topping_x = 1086
                topping_y = 331 + (80 + 12 + 80) * 3

            # Horizontal loop
            for i in range(1, 6):
                pag.click(topping_x, topping_y)
                time.sleep(0.2)
                self.__capture()

                # Each topping is 160x160 px, with 12 px spacing
                topping_x += 80 + 12 + 80
                counter   += 1

            # Move to the first column and the next row
            topping_x  = 1086
            topping_y += 80 + 12 + 80

            # Algorithm calculations
            row_number += 1
            if row_number % 4 == 0:
                block_number += 1