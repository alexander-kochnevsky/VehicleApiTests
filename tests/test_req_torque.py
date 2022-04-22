from typing import Tuple

import allure
import pytest

from framework.utils.asserts import assertions as asserts
from project.consts.acc_pedal_states import AccPedalStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.req_torque_states import ReqTorqueStates
from project.consts.signal_id import SignalId
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi
from tests.test_data import vehicle_test_data as test_data


@allure.feature('Request torque')
class TestRecTorque:
    @allure.issue('', 'Partially blocked by Bug #1')
    @allure.title('Test request torque states')
    @pytest.mark.parametrize("gear", [GearStates.DRIVE, GearStates.REVERSE])
    @pytest.mark.parametrize("test_param", test_data.REQ_TORQUE_DATA)
    def test_req_torque_states(self, vehicle_api: VehicleApi, test_param: Tuple[str, str], gear: str):
        acc_pedal_pos, expected_torque = test_param
        steps.stop_vehicle_and_select_gear(vehicle_api, gear)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        torque = vehicle_api.signals.get_signal(SignalId.REQ_TORQUE)
        asserts.are_equal(torque.value, expected_torque)

    @allure.title('Request torque blocked by gear')
    @pytest.mark.parametrize("gear", [GearStates.PARK, GearStates.NEUTRAL])
    @pytest.mark.parametrize("acc_pedal_pos", AccPedalStates.available_states())
    def test_req_torque_blocked_by_gear(self, vehicle_api: VehicleApi, acc_pedal_pos: str, gear: str):
        steps.stop_vehicle_and_select_gear(vehicle_api, gear)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        torque = vehicle_api.signals.get_signal(SignalId.REQ_TORQUE)
        asserts.are_equal(torque.value, ReqTorqueStates.REQ_0)

    @allure.title('Request torque blocked by brake')
    @pytest.mark.parametrize("gear", [GearStates.DRIVE, GearStates.REVERSE])
    @pytest.mark.parametrize("brake_state", [BrakeStates.ERROR, BrakeStates.PRESSED])
    @pytest.mark.parametrize("acc_pedal_pos", AccPedalStates.available_states())
    def test_req_torque_blocked_by_brake(self, vehicle_api: VehicleApi, acc_pedal_pos: str, gear: str,
                                         brake_state: str):
        steps.select_gear(vehicle_api, gear)
        steps.set_brake_state(vehicle_api, brake_state)
        steps.set_acc_pedal_pos(vehicle_api, acc_pedal_pos)
        torque = vehicle_api.signals.get_signal(SignalId.REQ_TORQUE)
        asserts.are_equal(torque.value, ReqTorqueStates.REQ_0)
