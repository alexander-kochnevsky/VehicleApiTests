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


@allure.feature('Battery')
class TestBattery:
    @allure.title('Test battery states')
    @pytest.mark.parametrize("test_param", test_data.BATTERY_DATA)
    def test_set_battery_states(self, vehicle_api: VehicleApi, test_param: Tuple[float, str]):
        voltage, expected_state = test_param
        vehicle_api.pins.update_pin(PinId.BATTERY_VOLTAGE, voltage)
        pin = vehicle_api.pins.get_pin(PinId.BATTERY_VOLTAGE)
        asserts.are_equal(pin.voltage, voltage)
        signal = vehicle_api.signals.get_signal(SignalId.BATTERY)
        asserts.are_equal(signal.value, expected_state)

    @allure.issue('', 'Bug #2, Bug #3')
    @allure.title('Test battery error state')
    @pytest.mark.parametrize("gear", GearStates.available_states())
    @pytest.mark.parametrize("acc_pedal_pos", AccPedalStates.available_states())
    def test_battery_error(self, vehicle_api: VehicleApi, gear: str, acc_pedal_pos: str):
        steps.stop_vehicle_and_select_gear(vehicle_api, gear)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        steps.set_battery_state(vehicle_api, BatteryStates.ERROR)
        pins = vehicle_api.pins.get_all_pins()
        for pin in pins:
            asserts.are_equal_soft(pin.voltage, 0)
        signals = vehicle_api.signals.get_all_signals()
        asserts.are_equal_soft(signals[SignalId.GEAR_POSITION].value, GearStates.NEUTRAL)
        asserts.are_equal_soft(signals[SignalId.BRAKE_PEDAL].value, BrakeStates.ERROR)
        asserts.are_equal_soft(signals[SignalId.ACC_PEDAL].value, AccPedalStates.ERROR)
        asserts.are_equal_soft(signals[SignalId.REQ_TORQUE].value, ReqTorqueStates.REQ_0)

    @allure.title('Test battery "Not Ready" state')
    @pytest.mark.parametrize("brake_pedal_pos", [BrakeStates.PRESSED, BrakeStates.RELEASED])
    @pytest.mark.parametrize("gear", GearStates.available_states())
    @pytest.mark.parametrize("acc_pedal_pos", AccPedalStates.available_states())
    def test_battery_not_ready(self, vehicle_api: VehicleApi, gear: str, acc_pedal_pos: str, brake_pedal_pos: str):
        steps.stop_vehicle_and_select_gear(vehicle_api, gear)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        steps.set_brake_state(vehicle_api, brake_pedal_pos)
        expected_signals = vehicle_api.signals.get_all_signals()
        steps.set_battery_state(vehicle_api, BatteryStates.NOT_READY)
        expected_signals[SignalId.GEAR_POSITION].value = GearStates.NEUTRAL
        expected_signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_0
        expected_signals[SignalId.BATTERY].value = BatteryStates.NOT_READY
        actual_signals = vehicle_api.signals.get_all_signals()
        asserts.are_equal(actual_signals, expected_signals)
