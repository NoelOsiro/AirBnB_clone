![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/14c5a9c3-6470-4ec7-ab5b-8c9c2ba61921)

# 🏡 AirBnB_clone

Welcome to the AirBnB Clone Solution! We've crafted a comprehensive solution to deploy a simplified version of the AirBnB website on your server. This solution covers all the fundamental concepts of higher-level programming.
![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/9a4ab926-f5b0-4434-97b2-0e802259ffc4)
![image](https://github.com/NoelOsiro/AirBnB_clone/assets/105745954/aeadd307-32ae-494d-ac86-f692a0d1dfb1)

## Solution Overview
📅 **Timeline**: From the start until the end of the first year.
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

- `**kwargs` enables you to pass a variable number of keyword arguments to a function or method.
- These arguments are collected into a dictionary, which can be accessed using their respective keys within the function.
- This is particularly useful when you need to pass a varying set of named parameters to a function.

Understanding and utilizing `*args` and `**kwargs` effectively can enhance the versatility and adaptability of your code, making it more robust and accommodating to different use cases.
