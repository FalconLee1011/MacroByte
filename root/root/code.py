from PyMata.pymata import PyMata
import time

timer = None

board = PyMata('/dev/ttyS0')
board.reset()
board.set_pin_mode(13,board.PWM,board.DIGITAL)

while timer < 10:
    timer = time.time()
    print("Hello, World !")
    board.digital_write(13, High)
    time.sleep(0.5)
    board.digital_write(13, Low)
