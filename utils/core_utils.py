import subprocess
import os
import sys
class CoreUtils:
    @staticmethod
    def core(ip):


        proc = subprocess.Popen('core\ConsoleApp1.exe',creationflags=subprocess.CREATE_NEW_CONSOLE,shell=True)
        proc.wait()
        print("OK")
