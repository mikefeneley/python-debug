import subprocess
import os
import signal
def test():
    print("HELLO")
    
class Debug:

    def __init__(self):
        pass

    def stop_process(self):
        pid = os.getpid()
        print(pid, "STOPPID")    
   
        os.kill(pid, signal.SIGSTOP)
        print("AFTER")
    def load(self, path):
        print(os.getpid(), "FIRST")
        self.process = subprocess.Popen(path, preexec_fn=self.stop_process)
        print("OTHER")
        if self.process:    
            
            print(self.process.pid, "HERE")
            print("OVER")
        else:
            print("Create failed")



if __name__ == '__main__':
    debug = Debug()
    debug.load("/bin/ls")
