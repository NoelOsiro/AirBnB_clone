import json

class FileStorage:
    """
    Handles serialization and deserialization of objects to/from a JSON file.
    """
    classes = {
        "BaseModel": BaseModel,
        "User": User,
    }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects (__objects).
        """
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
                    cls = eval(class_name)
                    self.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass
