import PIL.ImageGrab
import win32gui
import pyautogui

while True:
	color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 571 , 390)

	if color == 7002955:
		pyautogui.click()

