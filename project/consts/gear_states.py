from typing import List, Tuple, Dict


class GearStates:
    PARK: str = 'Park'
    NEUTRAL: str = 'Neutral'
    REVERSE: str = 'Reverse'
    DRIVE: str = 'Drive'

    __mapping: Dict[str, Tuple[float, float]] = {
        PARK: (0.67, 3.12),
        NEUTRAL: (1.48, 2.28),
        REVERSE: (2.28, 1.48),
        DRIVE: (3.12, 0.67)
    }

    @classmethod
    def available_states(cls) -> List[str]:
        return [cls.PARK, cls.NEUTRAL, cls.REVERSE, cls.DRIVE]

    @classmethod
    def get_voltages(cls, state: str) -> Tuple[float, float]:
        return cls.__mapping.get(state, 'Invalid battery state')
