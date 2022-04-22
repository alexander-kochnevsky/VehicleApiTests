import allure
import pytest

from framework.utils.asserts import assertions as asserts
from project.consts.pin_id import PinId
from project.test_clients.vehicle_api_clients import VehicleApi


@allure.feature('Negative Tests')
class TestNegative:
    @allure.title('Voltage drop on single pin')
    @pytest.mark.parametrize("pin_id", [PinId.GEAR_1, PinId.GEAR_2, PinId.ACC_PEDAL, PinId.BRAKE_PEDAL])
    def test_voltage_drop_on_single_pin(self, vehicle_api: VehicleApi, pin_id: int):
        expected_pins = vehicle_api.pins.get_all_pins()
        vehicle_api.pins.update_pin(pin_id, 0)
        changed_pin = next(x for x in expected_pins if x.pin_id == pin_id)
        changed_pin.voltage = 0
        actual_pins = vehicle_api.pins.get_all_pins()
        asserts.are_equal(actual_pins, expected_pins)
