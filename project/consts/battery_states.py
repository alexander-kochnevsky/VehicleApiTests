from typing import List, Dict


class BatteryStates:
    ERROR: str = 'Error'
    READY: str = 'Ready'
    NOT_READY: str = 'NotReady'

    __mapping: Dict[str, float] = {
        ERROR: 0,
        NOT_READY: 250,
        READY: 450
    }

    @classmethod
    def available_states(cls) -> List[str]:
        return [cls.ERROR, cls.READY, cls.NOT_READY]

    @classmethod
    def get_voltage(cls, state: str) -> float:
        return cls.__mapping.get(state, 'Invalid battery state')
