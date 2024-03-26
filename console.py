#!/usr/bin/python3
"""
this is the main console for our application
"""
import cmd
from models import classes, storage
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
        print(arg)
        if not self.checker(arg, ["n", 'ec']):
            return
        bss = classes[arg]()
        bss.save()
        print(bss.id)

    def do_show(self, model):
        """this method allows the show command to work"""

        

    def do_destroy(self, model):
        """this method allows the destroy command to remove an instance"""

        

    def do_all(self, model):
        """
        this method allows you dislay all instances of the model
        """

        

    def do_update(self, model):
        """this command allows you to updatean instance"""

        


if __name__ == "__main__":
    HBNBCommand().cmdloop()