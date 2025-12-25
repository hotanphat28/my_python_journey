"""Module providing a function printing greeting to user"""
import sys
from sys import argv

def run():
    print("Arguments provided:", sys.argv)
    if len(argv) == 2:
        print(f"hello, {argv[1]}")
    else:
        print("hello, World")

    for arg in argv[1:]:
        print(arg)
    
    # We won't use sys.exit() here as it would kill the main program
    if len(sys.argv) != 2:
        print("Missing command-line argument (simulated warning)")
    else:
        print(f"hello, {sys.argv[1]}")

if __name__ == "__main__":
    run()
