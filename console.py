#!/usr/bin/python3
""" Make the entry point to CMD """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Contain the commmanns of ours console

        Args:
            Inheritance from the class cmd
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ If there is empty line in the programm """
        pass

    # Ctrl + d = Quit the program
    do_EOF = do_quit

if __name__ == "__main__":
    """ Link the files """
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
