#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if __name__ == "__main__":
        num_args = len(argv) - 1  # subtract 1 to exclude the script name
        args_list = argv[1:] if num_args > 0 else []
        print("{} {}{}".format(
            num_args, "argument" if num_args == 1 else "arguments", ":"
            if num_args > 0 else "."))
        for i, arg in enumerate(args_list, start=1):
            print("{}: {}".format(i, arg))
