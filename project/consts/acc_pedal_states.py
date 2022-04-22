from typing import List, Dict


class AccPedalStates:
    ERROR: str = 'Error'
    POS_0: str = '0 %'
    POS_30: str = '30 %'
    POS_50: str = '50 %'
    POS_100: str = '100 %'

    __mapping: Dict[str, float] = {
        ERROR: 0.5,
        POS_0: 1.5,
        POS_30: 2,
        POS_50: 2.5,
        POS_100: 3,
    }

    @classmethod
    def available_states(cls) -> List[str]:
        return [cls.ERROR, cls.POS_0, cls.POS_30, cls.POS_50, cls.POS_100]

    @classmethod
    def get_voltage(cls, state: str) -> float:
        return cls.__mapping.get(state, 'Invalid battery state')
