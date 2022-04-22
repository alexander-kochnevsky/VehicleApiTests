from typing import Tuple

import allure
import pytest

from framework.utils.asserts import assertions as asserts
from project.consts.acc_pedal_states import AccPedalStates
from project.consts.battery_states import BatteryStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.pin_id import PinId
from project.consts.req_torque_states import ReqTorqueStates
from project.consts.signal_id import SignalId
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi
from tests.test_data import vehicle_test_data as test_data


@allure.feature('Brake')
class TestBrake:
    @allure.title('Test brake states')
    @pytest.mark.parametrize("test_param", test_data.BRAKE_DATA)
    def test_brake_states(self, vehicle_api: VehicleApi, test_param: Tuple[float, str]):
        voltage, expected_state = test_param
        vehicle_api.pins.update_pin(PinId.BRAKE_PEDAL, voltage)
        pin = vehicle_api.pins.get_pin(PinId.BRAKE_PEDAL)
        asserts.are_equal(pin.voltage, voltage)
        signal = vehicle_api.signals.get_signal(SignalId.BRAKE_PEDAL)
        asserts.are_equal(signal.value, expected_state)

    @allure.title('Test system state after pressing brake pedal')
    @pytest.mark.parametrize("acc_pedal_pos", AccPedalStates.available_states())
    @pytest.mark.parametrize("gear", GearStates.available_states())
    @pytest.mark.parametrize("battery_state", [BatteryStates.READY, BatteryStates.NOT_READY])
    def test_brake_state_pressed(self, vehicle_api: VehicleApi, gear: str, acc_pedal_pos: str, battery_state: str):
        steps.stop_vehicle_and_select_gear(vehicle_api, gear)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        steps.set_battery_state(vehicle_api, BatteryStates.NOT_READY)
        expected_signals = vehicle_api.signals.get_all_signals()
        expected_signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_0
        expected_signals[SignalId.BRAKE_PEDAL].value = BrakeStates.PRESSED
        steps.press_brake(vehicle_api)
        actual_signals = vehicle_api.signals.get_all_signals()
        asserts.are_equal(actual_signals, expected_signals)
