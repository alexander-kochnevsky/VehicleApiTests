import json
from typing import List

import humps

from project.models.pin import Pin


class Pins:
    def __init__(self, pins: List[Pin]):
        self.pins = pins

    def to_json(self) -> str:
        """Converts the Pins instance to a JSON string."""
        return json.dumps(self, default=lambda o: o.__dict__)

    def __getattribute__(self, item):
        if item == '__dict__':
            return {humps.pascalize(x): y for x, y in object.__getattribute__(self, item).items()}
        else:
            return object.__getattribute__(self, item)
