import humps


class Pin:
    """
    A class to represent a Pin object for vehicle API.

    Pin example in JSON:{ "Name": "Gear_1","PinId": 1,"Voltage": 0.01 }

    Args:
        name (str): Pin name
        pin_id (int): Pin Id
        voltage (float): Pin voltage
    """

    def __init__(self, pin_id: int, voltage: float, name: str = None):
        self.name = name
        self.pin_id = pin_id
        self.voltage = voltage

    def __eq__(self, other):
        return self.name == other.name and self.pin_id == other.pin_id and self.voltage == other.voltage

    def __repr__(self):
        return f'name: {self.name}, pin_id: {self.pin_id}, voltage: {self.voltage}'

    def __getattribute__(self, item):
        if item == '__dict__':
            return {humps.pascalize(x): y for x, y in object.__getattribute__(self, item).items()}
        else:
            return object.__getattribute__(self, item)

    @staticmethod
    def decode_pin(dct: dict):
        """
        Converts dictionary to Pin instance, can be passed as object_hook parameter in requests methods.

        Args:
            dct (dict): Dictionary with pin fields

        Returns:
            Pin instance
        """
        return Pin(dct.get('PinId'), dct.get('Voltage'), dct.get('Name'))
