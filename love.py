import os
import math
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Red color code
red = "\033[91m"
reset = "\033[0m"

# Draw heart with slow animation
for y in range(15, -15, -1):
    row = ""
    for x in range(-30, 30):
        x_scaled = x * 0.05
        y_scaled = y * 0.1
        a = x_scaled**2 + y_scaled**2 - 1
        if a**3 - x_scaled**2 * y_scaled**3 <= 0:
            row += f"{red}*{reset}"  # Red asterisk
        else:
            row += " "
    print(row)
    time.sleep(0.05)

# Final romantic message 💌
time.sleep(0.5)
print(f"{red}{'i love you <3'.center(60)}{reset}")
