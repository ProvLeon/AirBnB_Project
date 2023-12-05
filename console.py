#!/usr/bin/python3

import cmd


class Console(cmd.Cmd):
    """
    console class for AirBnB project shell
    """

    prompt = "(HSH>>)$ "

    def do_show(self):
        """
        prints the string representation of an object
        """
        pass

    def do_quit(self, line):
        """
        quit the shell
        """
        return True

    def do_create(self, line):
        """create an instance of BaseModel and saves it to JSON file

        Args:
            line (any): the class name
        """
        pass

    def do_EOF(self, line):
        """EOF command

        Args:
            line (any): EOF

        Returns:
            Boolean: returns true
        """
        print("\n")
        return True

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass


if __name__ == "__main__":
    try:
        Console().cmdloop()
    except KeyboardInterrupt:
        print("\nKeyboard Interruption")
