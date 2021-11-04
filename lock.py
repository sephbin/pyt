import ctypes
import random
test = random.randint(1, 50)
if test == 1:
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Error', 'Error', 0)
    ctypes.windll.user32.LockWorkStation()
a=x