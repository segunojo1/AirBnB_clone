classes = {}


def get_classes():
    from models.city import City
    from models.user import User
    from models.base_model import BaseModel
    from models.review import Review
    from models.place import Place
    from models.state import State
    from models.amenity import Amenity

    global classes
    classes.update({
        "City": City,
        "User": User,
        "BaseModel": BaseModel,
        "Review": Review,
        "Place": Place,
        "State": State,
        "Amenity": Amenity
    })