#!/usr/bin/python3
"""
this is the main console for our application
"""
import cmd
from .models.basemodel import BaseModel


class HBNBCommand(cmd.Cmd):
    """it is the hbnb command console interface
    Args: cmd.Cmd very special
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """This exits the program"""
        return True

    def do_EOF(self, arg):
        """This helps to end the program"""
        print("")
        return True

    def emptyline(self):
        """This does nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """This helps in the running the create command"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()