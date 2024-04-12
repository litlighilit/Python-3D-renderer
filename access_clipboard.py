
import os, subprocess
if os.name == 'nt':
    def set_clipboard(s):
        subprocess.run(["powershell", "Set-Clipboard", " -Value", s])
else:
    def is_command_available(cmd):
        ret = subprocess.run(['which', cmd], stdout=subprocess.PIPE)
        return ret.returncode == 0
    _CLIP_CMD = 'xclip'
    _HAS_CLIP = False
    if not is_command_available(_CLIP_CMD):
        import warnings
        warnings.warn(f'{_CLIP_CMD} is not available, \
                    please install it to support set_clipboard')
    else:
        _HAS_CLIP = True

    def set_clipboard(s):
        if _HAS_CLIP:
            p = subprocess.Popen([_CLIP_CMD], stdin=subprocess.PIPE, text=True)
            p.stdin.write(s)
            p.flush()

