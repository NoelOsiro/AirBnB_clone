import json


class FileStorage:
    """
    Handles serialization and deserialization of objects to/from a JSON file.
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def classes(self):
        """
        Returns a dictionary of supported classes.
        Key: class name (string)
        Value: corresponding class (class)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def all(self, cls=None):
        """
        Return a dictionary of objects.

        Args:
            cls (class, str): Class name or class object to filter the objects.

        Returns:
            dict: Dictionary of objects.
        """
        if cls:
            if isinstance(cls, str):
                class_mapping = self.classes()
                if cls not in class_mapping:
                    raise NameError(f"Class '{cls}' doesn't exist.")
                cls = class_mapping[cls]

            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds an object to the dictionary (__objects).

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exists).
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = self.classes().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass
