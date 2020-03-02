def on_key_press(key):
    print('Pressed Key %s' % key)
    if key == keyboard.KeyCode(char='w'):
        print("yay")
        client.publish("mads-ln@hotmail.dk/ev3test","Det virker!")
with keyboard.Listener(on_press = on_key_press) as listener:
    listener.join()

def on_key_release(key):
    print('Released Key %s' % key)
    if key == keyboard.KeyCode(char='w'):
        print("yay")
        client.publish("mads-ln@hotmail.dk/ev3test","Det virker!")
with keyboard.Listener(on_release = on_key_release) as listener:
    listener.join()