
![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/14c5a9c3-6470-4ec7-ab5b-8c9c2ba61921)

# 🏡 AirBnB_clone



## Documentation

## Solution Overview
📅 **Timeline**: From the start until the end of the first year.
![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/9a4ab926-f5b0-4434-97b2-0e802259ffc4)
![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/f163940b-ccf3-4095-b239-1bc16b0f1e45)

Here's what our solution offers:

1. **Command Interpreter (Console) 🖥️**
   - Create a data model.
   - Manage objects through a console/command interpreter.
   - Store and persist objects to a JSON file.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/cda72973-3b86-40de-97fe-000ea1ffb370)

2. **Storage Engine 📦**
   - Develop a robust storage system.
   - Abstract the storage and persistence of objects.
   - Easily switch between storage types without code updates.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/28a50445-6ce8-4ecd-8520-0f32f435a616)

3. **Web Static 🌐**
   - Learn HTML/CSS.
   - Create HTML templates for your application.
   - Create templates for each object.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/de643740-7d94-4042-9481-f5a8695d99e5)

4. **MySQL Storage 🗄️**
   - Transition from file storage to Database storage.
   - Map your models to database tables using an Object-Relational Mapping (O.R.M.).

5. **Web Framework - Templating 🚀**
   - Build your first web server in Python.
   - Dynamically populate static HTML files with objects from files or databases.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/d971b12a-924d-46e9-abdc-92dd70ada234)

6. **RESTful API 🌐**
   - Expose all stored objects through a JSON web interface.
   - Manipulate objects via a RESTful API.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/a7025d14-e518-46f5-b995-06fda6946d3c)

7. **Web Dynamic 🔄**
   - Learn JQuery.
   - Load objects from the client side using your own RESTful API.
     ![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/15812392-b38d-49bd-8115-1c3dce87ae62)


## Solution Structure 📂
- 📁 `models`: Contains all classes used in the solution, representing objects/instances.
- 📁 `tests`: Houses all unit tests.
- 📄 `console.py`: The entry point for the command interpreter.
- 📄 `models/base_model.py`: The base class for all models, with common elements like attributes `id`, `created_at`, and `updated_at`, and methods `save()` and `to_json()`.
- 📁 `models/engine`: Stores storage classes, initially just `file_storage.py`.

## Storage Solution 💾
Persistence is key for web applications, ensuring data continuity between program executions. Our solution covers two types of storage: file and database, with the initial focus on file storage.

Why separate "storage management" from "model"? This architecture promotes modularity and independence, facilitating the swapping of storage systems without extensive code modification.

## Class Attributes 🧾
We emphasize using class attributes for objects, rather than instance attributes, for several reasons:
1. Provides clear class descriptions.
2. Offers default attribute values.
3. Ensures consistent model behavior for both file and database storage in the future.

## File Storage and JSON Serialization

In this section, we'll delve into the critical aspect of file storage and JSON serialization. This process involves saving your objects/instances to a file when created or updated in the command interpreter and restoring them when the interpreter is started again.

### Saving Objects to a File

To save Python objects to a file, follow these steps:

1. **Convert to Serializable Data Structure**: Use the method `my_instance.to_json()` to convert an instance into a Python built-in serializable data structure, typically a dictionary.

2. **Serialize to JSON Format**: Convert this data structure to a string in JSON format (though other formats like YAML or XML can be used). For our purposes, this can be achieved with `my_string = JSON.dumps(my_dict)`.

3. **Write to Disk**: Write this string to a file on disk, which serves as your storage medium.

### Restoring Objects from a File

Restoring objects from a file involves the reverse process:

1. **Read from Disk**: Read a string from a file on disk. This string represents the serialized data, typically in JSON format.

2. **Deserialize to Data Structure**: Convert this string to a data structure. Since it's in JSON format, you can easily achieve this with `my_dict = JSON.loads(my_string)`.

3. **Convert to Instance**: Finally, convert this data structure back into an instance of the relevant class using `my_instance = MyObject(my_dict)`.

## *args and **kwargs

In programming, `*args` and `**kwargs` are special constructs used to pass a variable number of arguments to functions or methods. They are widely used in Python and play an essential role in flexible and dynamic code.

### *args (Positional Arguments)

- `*args` allows you to pass a variable number of non-keyword (positional) arguments to a function or method.
- These arguments are collected into a tuple, which can be iterated over or processed as needed within the function.
- This flexibility enables you to call functions with different numbers of arguments.

### **kwargs (Keyword Arguments)




## Setup and Installation

### Description of the Command Interpreter
The project includes a command interpreter (Console) that provides the following functionalities:
- Create a data model.
- Manage objects through a console/command interpreter.
- Store and persist objects to a JSON file.

### How to Start It
To start the AirBnB Clone Solution, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project's root directory.
3. Run the `console.py` script.

### How to Use It
Once the command interpreter is running, you can use it to perform various operations, including creating and managing objects. Here are some basic commands to get you started:
- `create <class_name>`: Create an instance of the specified class.
- `show <class_name> <object_id>`: Show details of a specific object.
- `all <class_name>`: List all objects of a specific class.
- `update <class_name> <object_id> <attribute_name> "<new_value>"`: Update an attribute of an object.

### Code Examples
Here are some code examples to demonstrate how to use the command interpreter:
```bash
$ ./console.py
(hbnb) create User
3fb9d628-6b95-4bdf-91e4-19b2f4341eb9
(hbnb) show User 3fb9d628-6b95-4bdf-91e4-19b2f4341eb9
[User] (3fb9d628-6b95-4bdf-91e4-19b2f4341eb9) {'id': '3fb9d628-6b95-4bdf-91e4-19b2f4341eb9', 'created_at': datetime.datetime(2023, 10, 10, 12, 0, 0), 'updated_at': datetime.datetime(2023, 10, 10, 12, 0, 0)}
(hbnb) all User
["[User] (3fb9d628-6b95-4bdf-91e4-19b2f4341eb9) {'id': '3fb9d628-6b95-4bdf-91e4-19b2f4341eb9', 'created_at': datetime.datetime(2023, 10, 10, 12, 0, 0), 'updated_at': datetime.datetime(2023, 10, 10, 12, 0, 0)}"]
(hbnb) update User 3fb9d628-6b95-4bdf-91e4-19b2f4341eb9 first_name "John"
(hbnb) show User 3fb9d628-6b95-4bdf-91e4-19b2f4341eb9
[User] (3fb9d628-6b95-4bdf-91e4-19b2f4341eb9) {'id': '3fb9d628-6b95-4bdf-91e4-19b2f4341eb9', 'created_at': datetime.datetime(2023, 10, 10, 12, 0, 0), 'updated_at': datetime.datetime(2023, 10, 10, 12, 1, 0), 'first_name': 'John'}
```

### Authors
Please refer to the `AUTHORS` file at the root of the repository to see a list of all individuals who have contributed content to the project. The format of this file should follow the Docker [AUTHORS page](https://github.com/NoelOsiro/AirBnB_clone/blob/main/AUTHORS).

### Using Branches and Pull Requests
We encourage the use of branches and pull requests on GitHub to help organize and coordinate work within the team. This approach ensures that contributions are reviewed and integrated effectively.

### Solution Overview
![Solution Overview](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/f163940b-ccf3-4095-b239-1bc16b0f1e45)

The AirBnB Clone Solution offers a comprehensive set of features, including a command interpreter, storage engine, web static, MySQL storage, web framework templating, RESTful API, and web dynamic functionalities. Each aspect of the solution is designed to help you learn and implement key concepts in programming and web development.
## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## License

This project is licensed under the [MIT License](LICENSE).
## Roadmap

- Additional browser support
- Add more integrations
- Add SNS, SES functionality

## Authors

For any inquiries or questions, please reach out to:

Noel Osiro
- Email: [noelosiroski@gmail.com](mailto:noelosiroski@gmail.com) ![Gmail](https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white&style=flat-square)
- Twitter: [@Osiroski](https://twitter.com/NoelOsiro) ![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white&style=flat-square)
- LinkedIn: [Noel Osiro](https://www.linkedin.com/in/noelosiroski/) ![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=flat-square)

Feel free to contact me for any feedback, collaboration opportunities, or if you have any questions related to the Dental Clinic Management System project or technology stack. I'm always eager to connect and learn from the community! 🌟📧🐦
