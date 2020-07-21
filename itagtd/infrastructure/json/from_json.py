import inspect
from typing import Dict, List


def from_json(data, cls):
    annotations: dict = cls.__annotations__ if hasattr(cls, '__annotations__') else None
    if issubclass(cls, List):
        list_type = cls.__args__[0]
        instance: list = list()
        for value in data:
            instance.append(from_json(value, list_type))
        return instance

    if issubclass(cls, Dict):
        key_type = cls.__args__[0]
        val_type = cls.__args__[1]
        instance: dict = dict()
        for key, value in data.items():
            instance.update(from_json(key, key_type), from_json(value, val_type))
        return instance

    instance: cls = cls()
    for name, value in data.items():
        field_type = annotations.get(name)
        if inspect.isclass(field_type) and isinstance(value, (dict, tuple, list, set, frozenset)):
            setattr(instance, name, from_json(value, field_type))
        else:
            setattr(instance, name, value)

    return instance
