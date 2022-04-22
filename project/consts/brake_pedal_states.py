from typing import List, Dict


class BrakeStates:
    ERROR: str = 'Error'
    PRESSED: str = 'Pressed'
    RELEASED: str = 'Released'

    __mapping: Dict[str, float] = {
        ERROR: 0.5,
        PRESSED: 1.5,
        RELEASED: 2.5
    }

    @classmethod
    def available_states(cls) -> List[str]:
        return [cls.ERROR, cls.PRESSED, cls.RELEASED]

    @classmethod
    def get_voltage(cls, state: str) -> float:
        return cls.__mapping.get(state, 'Invalid battery state')
