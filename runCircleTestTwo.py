import pyautogui
import math
import time

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Constants
start_x, start_y = screen_width // 2, screen_height // 2 + 18
offset = 18
center_x, center_y = 960, 753
radius = 320
duration = 5  # Adjust the duration as needed
initial_delay = 3  # Adjust the initial delay as needed
# Calculate the starting point on the edge of the circle
start_circle_x = start_x + radius
start_circle_y = start_y
# Wait for three seconds before the initial move
time.sleep(initial_delay)

# Move the mouse to the starting position
pyautogui.moveTo(start_x, start_y)

# Click and hold the mouse button
pyautogui.mouseDown()

# Release mouse button
pyautogui.mouseUp()

# Move the mouse to the starting position
pyautogui.moveTo(start_circle_x, start_circle_y)

# Click and hold the mouse button
pyautogui.mouseDown()

# Move the mouse to the center and draw the circle
start_time = time.time()
while time.time() - start_time < duration:
    angle = (time.time() - start_time) * 2 * math.pi / duration
    x = start_x + int(radius * math.cos(angle))
    y = start_y + int(radius * math.sin(angle))
    pyautogui.moveTo(x, y)

# Release the mouse button
pyautogui.mouseUp()
