from typing import List


class ReqTorqueStates:
    REQ_0: str = '0 Nm'
    REQ_3000: str = '3000 Nm'
    REQ_5000: str = '5000 Nm'
    REQ_10000: str = '10000 Nm'

    @classmethod
    def available_states(cls) -> List[str]:
        return [cls.REQ_0, cls.REQ_3000, cls.REQ_5000, cls.REQ_10000]
