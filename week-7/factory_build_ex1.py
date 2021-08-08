'''
 https://realpython.com/factory-method-python/
 '''

class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

'''
The difference is in the interface that exposes to support creating any type of object. The builder parameter can be any object that implements the callable interface. This means a Builder can be a function, a class, or an object that implements .__call__().

The .create() method requires that additional arguments are specified as keyword arguments. This allows the Builder objects to specify the parameters they need and ignore the rest in no particular order. For example, you can see that create_local_music_service() specifies a local_music_location parameter and ignores the rest.
'''

import json
import xml.etree.ElementTree as et

class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')
