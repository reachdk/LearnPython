import sys


def hello():
    name = ("Hi %s, I have %d donuts") %("Alice", 42)
    print(name)


def main():
   hello()

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()
