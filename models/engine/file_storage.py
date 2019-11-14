#!/usr/bin/python3
"""Module FileStorage"""

import json
import os


class FileStorage:
        """ Definition of FileStorage class """
        __file_path = "file.json"
        __objects = {}

        def all(self):
            """
               Returns:
                     the dictionary __objects
            """
            return self.__objects

        def new(self, obj):
            """ Sets in __objects the obj with key <obj class name>.id """
            key = str(obj.__class__.__name__ + "." + obj.id)
            self.__objects[key] = obj

        def save(self):
            """ Serializes __objects to the JSON file """
            from models.base_model import BaseModel
            with open(self.__file_path, "w") as f:
                dict_of_dicts = {}
                for k, v in self.__objects.items():                    
                    dict_of_dicts[k] = v.to_dict()
                f.write(json.dumps(dict_of_dicts))

        def reload(self):
            """ Deserializes the JSON file to __objects if it exists """
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            try:
                with open(self.__file_path, "r") as f:
                    dict_of_dicts = json.loads(f.read())
                    for k, d in dict_of_dicts.items():
                        if(d['__class__'] == "BaseModel"):
                            b = BaseModel(**d)
                            FileStorage.__objects[k] = b
                        elif(d['__class__'] == "User"):
                            u = User(**d)
                            FileStorage.__objects[k] = u
                        elif(d['__class__'] == "State"):
                            s = State(**d)
                            FileStorage.__objects[k] = s
                        elif(d['__class__'] == "City"):
                            c = City(**d)
                            FileStorage.__objects[k] = c
                        elif(d['__class__'] == "Amenity"):
                            a = Amenity(**d)
                            FileStorage.__objects[k] = a
                        elif(d['__class__'] == "Place"):
                            p = Place(**d)
                            FileStorage.__objects[k] = p
                        elif(d['__class__'] == "Review"):
                            r = Review(**d)
                            FileStorage.__objects[k] = r
            except:
                pass
