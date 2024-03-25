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
        """show command to display information about a specific instance"""

        if not self.checker(model, ["n", "l", "ec", "es"]):
            return
        cls, key = model.split()
        print(classes[cls].show(key))

    def do_destroy(self, model):
        """destroy command to remove a specific instance"""

        if not self.checker(model, ["n", "l", "ec", "es"]):
            return
        cls, key = model.split()
        classes[cls].destroy(key)

    def do_all(self, model):
        """
        all command to display all instances of a specific model or
        all instances across all models if none is
        specified
        """

        if model and not self.checker(model, ["ec"]):
            return
        if model:
            print(classes[model].all())
        else:
            print(storage.get_all())

    def do_update(self, model):
        """update command to modify an instance attribute value"""

        keys = ["n", "l", "ec", "es", "a", "v"]
        if not self.checker(model, keys):
            return
        extras = model.split()
        classes[extras[0]].update(extras[1], extras[2], extras[3])


if __name__ == "__main__":
    HBNBCommand().cmdloop()