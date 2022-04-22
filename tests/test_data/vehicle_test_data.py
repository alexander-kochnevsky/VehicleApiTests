from typing import Tuple, List

from project.consts.acc_pedal_states import AccPedalStates
from project.consts.battery_states import BatteryStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.req_torque_states import ReqTorqueStates

BATTERY_DATA: List[Tuple[float, str]] = [
    (0, BatteryStates.ERROR),
    (0.01, BatteryStates.NOT_READY),
    (400, BatteryStates.NOT_READY),
    (400.01, BatteryStates.READY),
    (800, BatteryStates.READY),
    (800.01, BatteryStates.ERROR)
]

BRAKE_DATA: List[Tuple[float, str]] = [
    (0, BrakeStates.ERROR),
    (0.99, BrakeStates.ERROR),
    (1, BrakeStates.PRESSED),
    (1.99, BrakeStates.PRESSED),
    (2, BrakeStates.RELEASED),
    (2.99, BrakeStates.RELEASED),
    (3, BrakeStates.ERROR)
]

ACC_PEDAL_DATA: List[Tuple[float, str]] = [
    (0, AccPedalStates.ERROR),
    (0.99, AccPedalStates.ERROR),
    (1, AccPedalStates.POS_0),
    (1.99, AccPedalStates.POS_0),
    (2, AccPedalStates.POS_30),
    (2.49, AccPedalStates.POS_30),
    (2.5, AccPedalStates.POS_50),
    (2.99, AccPedalStates.POS_50),
    (3, AccPedalStates.POS_100),
    (3.49, AccPedalStates.POS_100),
    (3.5, AccPedalStates.ERROR)
]

REQ_TORQUE_DATA: List[Tuple[str, str]] = [
    (AccPedalStates.ERROR, ReqTorqueStates.REQ_0),
    (AccPedalStates.POS_0, ReqTorqueStates.REQ_0),
    (AccPedalStates.POS_30, ReqTorqueStates.REQ_3000),
    (AccPedalStates.POS_50, ReqTorqueStates.REQ_5000),
    (AccPedalStates.POS_100, ReqTorqueStates.REQ_10000)
]

GEARS_DATA: List[Tuple[float, float, str]] = [
    (0.67, 3.12, GearStates.PARK),
    (1.48, 2.28, GearStates.NEUTRAL),
    (2.28, 1.48, GearStates.REVERSE),
    (3.12, 0.67, GearStates.DRIVE)
]
