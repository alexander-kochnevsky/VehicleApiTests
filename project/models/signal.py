class Signal:
    """
    A class to represent a Signal object for vehicle API.

    Signal example in JSON: { "Name": "GearPosition","SigId": 1,"Value": "Neutral" }

    Args:
        name (str): Signal name
        sig_id (int): Signal Id
        value (str): Signal value
    """

    def __init__(self, name: str, sig_id: int, value: str):
        self.name = name
        self.value = value
        self.sig_id = sig_id

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value and self.sig_id == other.sig_id

    def __repr__(self):
        return f'Name: {self.name}, Value: {self.value}, SigId: {self.sig_id}'

    @staticmethod
    def decode_signal(dct: dict):
        """
        Converts dictionary to Signal instance, can be passed as object_hook parameter in requests methods.

        Args:
            dct (dict): Dictionary with signal fields

        Returns:
            Signal instance
        """
        return Signal(dct.get('Name'), dct.get('SigId'), dct.get('Value'))
