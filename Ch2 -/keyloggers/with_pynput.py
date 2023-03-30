from pynput import keyboard, mouse

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")
    if key == keyboard.Key.esc:
        return False

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        print(f"Mouse released at ({x}, {y}) with {button}")

with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener:
    with mouse.Listener(on_move=on_move, on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()