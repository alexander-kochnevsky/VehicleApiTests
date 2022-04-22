from typing import Tuple

import allure
import pytest

from framework.utils.asserts import assertions as asserts
from project.consts.battery_states import BatteryStates
from project.consts.pin_id import PinId
from project.consts.signal_id import SignalId
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi
from tests.test_data import vehicle_test_data as test_data


@allure.issue('', 'Bug #1')
@allure.feature('Accelerator pedal')
class TestAccPedal:
    @allure.title('Test Accelerator pedal state')
    @pytest.mark.parametrize("battery_state", [BatteryStates.READY, BatteryStates.NOT_READY])
    @pytest.mark.parametrize("test_param", test_data.ACC_PEDAL_DATA)
    def test_acc_pedal_states(self, vehicle_api: VehicleApi, test_param: Tuple[float, str], battery_state: str):
        steps.set_battery_state(vehicle_api, battery_state)
        voltage, expected_pedal_state = test_param
        vehicle_api.pins.update_pin(PinId.ACC_PEDAL, voltage)
        pin = vehicle_api.pins.get_pin(PinId.ACC_PEDAL)
        asserts.are_equal(pin.voltage, voltage)
        signal = vehicle_api.signals.get_signal(SignalId.ACC_PEDAL)
        asserts.are_equal(signal.value, expected_pedal_state)
