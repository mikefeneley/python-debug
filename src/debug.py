import subprocess
import os
def test():
    print("TEST")

class Debug:

    def __init__(self):
        pass

    def load(self, path = "/bin/ls"):
        print(os.geteuid())
        self.process = subprocess.Popen(path)
        if self.process:
            print(self.process.pid)
        else:
            os.getpid()
if __name__ == '__main__':
    debug = Debug()
    debug.load("/bin/ls")
