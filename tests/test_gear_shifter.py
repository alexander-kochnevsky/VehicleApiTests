import allure
import pytest

from framework.utils.asserts import assertions as asserts
from project.consts.acc_pedal_states import AccPedalStates
from project.consts.battery_states import BatteryStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.signal_id import SignalId
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi


@allure.feature('Gear shifter')
class TestGearShifter:
    @allure.title('Test gear shifter states')
    @pytest.mark.parametrize("gear", GearStates.available_states())
    def test_gear_shifter_states(self, vehicle_api: VehicleApi, gear: str):
        steps.select_gear(vehicle_api, gear)
        actual_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        asserts.are_equal(actual_gear_pos.value, gear)

    @allure.title('Gear shifter blocked by accelerator pedal')
    @pytest.mark.parametrize("acc_pedal_pos", [AccPedalStates.POS_30, AccPedalStates.POS_50, AccPedalStates.POS_100,
                                               AccPedalStates.ERROR])
    @pytest.mark.parametrize("gear", GearStates.available_states())
    def test_gears_blocked_by_acc_pedal(self, vehicle_api: VehicleApi, gear: str, acc_pedal_pos: str):
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        steps.press_brake(vehicle_api)
        previous_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        steps.select_gear(vehicle_api, gear)
        actual_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        asserts.are_equal(actual_gear_pos.value, previous_gear_pos.value)

    @allure.title('Gear shifter blocked by battery')
    @pytest.mark.parametrize("battery_state", [BatteryStates.ERROR, BatteryStates.NOT_READY])
    @pytest.mark.parametrize("gear", GearStates.available_states())
    def test_gears_blocked_by_battery(self, vehicle_api: VehicleApi, gear: str, battery_state: str):
        steps.set_battery_state(vehicle_api, battery_state)
        previous_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        steps.select_gear(vehicle_api, gear)
        actual_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        asserts.are_equal(actual_gear_pos.value, previous_gear_pos.value)

    @allure.title('Gear shifter blocked by brake pedal')
    @pytest.mark.parametrize("brake_pedal_state", [BrakeStates.ERROR, BrakeStates.RELEASED])
    @pytest.mark.parametrize("gear", GearStates.available_states())
    def test_gears_blocked_by_brake(self, vehicle_api: VehicleApi, gear: str, brake_pedal_state: str):
        steps.set_brake_state(vehicle_api, brake_pedal_state)
        previous_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        steps.select_gear(vehicle_api, gear)
        actual_gear_pos = vehicle_api.signals.get_signal(SignalId.GEAR_POSITION)
        asserts.are_equal(actual_gear_pos.value, previous_gear_pos.value)
