###################################################
#                                                 #
# Project: Catherine (Module: Executable Dump)    #
# File: main.py                                   #
#                                                 #
# Author(s): {                                    #
#   Hifumi1337 <https://github.com/Hifumi1337>    #
# }                                               #
#                                                 # 
###################################################

from subprocess import getoutput
import pefile

VERSION = "0.1.8"

file_loc = input("🦀 Location of file: ")

try:
    try:
        pe = pefile.PE(str(file_loc))
    except FileNotFoundError:
        print("\nUnable to locate file. Please make sure the path is correct\n")
        exit(-1)
except pefile.PEFormatError:
    print("\nWrong exec format. Module only accepts Windows exec format\n")
    exit(-1)

class ExeDump:
    def bit_identifier() -> bool:
        if hex(pe.OPTIONAL_HEADER.Magic) == '0x10b':
            return False
        elif hex(pe.OPTIONAL_HEADER.Magic) == '0x20b':
            return True

    def exe_dump(self):
        print("\nFile Information")
        print(f"Magic Number (int): {pe.OPTIONAL_HEADER.Magic} (hex: {hex(pe.OPTIONAL_HEADER.Magic)})")

        if EXE.bit_identifier():
            print(f"Binary info: {hex(pe.OPTIONAL_HEADER.Magic)} (64-bit)")
        elif EXE.bit_identifier() != True:
            print(f"Binary info: {hex(pe.OPTIONAL_HEADER.Magic)} (32-bit)")

        print(f"TimeDateStamp: {pe.FILE_HEADER.dump_dict()['TimeDateStamp']['Value'].split('[')[1][:-1]}\n")

        whoami = getoutput("whoami")

        print("Available options")
        print("dump: Dumps information about the binary. This includes sections, headers, etc. for studying the header information\n")
        print("exit: Closes prompt\n")
        print("help: Displays this help menu\n")

        while True:
            exe_shell = input(f"{whoami}@EXE[🦀 Catherine Framework 🦀]:~$ ")

            if exe_shell == "dump" or exe_shell == "Dump":
                with open("header_dump.log", "w") as f:
                    f.write(pe.dump_info())
            elif exe_shell == "help":
                print("\nAvailable options")
                print("dump: Dumps information about the binary. This includes sections, headers, etc. for studying the header information\n")
            elif exe_shell == "exit" or exe_shell == "quit":
                exit(0)

if __name__ == '__main__':
    EXE = ExeDump()

    try:
        EXE.exe_dump()
    except NameError:
        pass