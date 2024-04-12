
import os, threading
if os.name == 'nt':
    import msvcrt
    getch = msvcrt.getwch
else:
    import termios, tty
    from sys import stdin
    from atexit import register
    _in_fd = stdin.fileno()
    _old_settings = termios.tcgetattr(_in_fd)
    def set_input_raw():
        tty.setraw(_in_fd)
    set_input_raw()
    def unset_input_raw():
        termios.tcsetattr(_in_fd, 
            termios.TCSADRAIN, _old_settings)
    register(unset_input_raw)
    def getch():
        return stdin.read(1)

def take_key():
    global key_GL, command_mode_GL
    while True:
        if not command_mode_GL:
            key_GL = getch()
        if key_GL == "Q":
            break
        elif key_GL == "/":
            command_mode_GL = True

global key_GL, command_mode_GL
key_GL, command_mode_GL = None, False
threading.Thread(target=take_key, daemon=True).start()