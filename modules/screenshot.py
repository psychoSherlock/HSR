from pyautogui import screenshot


def snapScreen(path):
    img = screenshot()
    img.save(path)
    return path
