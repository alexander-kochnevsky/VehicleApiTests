import allure

from framework.utils.asserts import assertions as asserts
from project.consts.acc_pedal_states import AccPedalStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.req_torque_states import ReqTorqueStates
from project.consts.signal_id import SignalId
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi


@allure.feature('E2E Tests')
class TestE2e:
    @allure.title('Smoke driving cycle test')
    def test_driving_cycle(self, vehicle_api: VehicleApi):
        signals = vehicle_api.signals.get_all_signals()

        steps.select_gear(vehicle_api, GearStates.DRIVE)
        signals[SignalId.GEAR_POSITION].value = GearStates.DRIVE
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.release_brake(vehicle_api)
        signals[SignalId.BRAKE_PEDAL].value = BrakeStates.RELEASED
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.set_acc_pedal_pos(vehicle_api, AccPedalStates.POS_50)
        signals[SignalId.ACC_PEDAL].value = AccPedalStates.POS_50
        signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_5000
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.set_acc_pedal_pos(vehicle_api, AccPedalStates.POS_0)
        signals[SignalId.ACC_PEDAL].value = AccPedalStates.POS_0
        signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_0
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.press_brake(vehicle_api)
        signals[SignalId.BRAKE_PEDAL].value = BrakeStates.PRESSED
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.select_gear(vehicle_api, GearStates.NEUTRAL)
        signals[SignalId.GEAR_POSITION].value = GearStates.NEUTRAL
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.select_gear(vehicle_api, GearStates.REVERSE)
        signals[SignalId.GEAR_POSITION].value = GearStates.REVERSE
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.release_brake(vehicle_api)
        signals[SignalId.BRAKE_PEDAL].value = BrakeStates.RELEASED
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.set_acc_pedal_pos(vehicle_api, AccPedalStates.POS_30)
        signals[SignalId.ACC_PEDAL].value = AccPedalStates.POS_30
        signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_3000
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.set_acc_pedal_pos(vehicle_api, AccPedalStates.POS_0)
        signals[SignalId.ACC_PEDAL].value = AccPedalStates.POS_0
        signals[SignalId.REQ_TORQUE].value = ReqTorqueStates.REQ_0
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.press_brake(vehicle_api)
        signals[SignalId.BRAKE_PEDAL].value = BrakeStates.PRESSED
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.select_gear(vehicle_api, GearStates.PARK)
        signals[SignalId.GEAR_POSITION].value = GearStates.PARK
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)

        steps.release_brake(vehicle_api)
        signals[SignalId.BRAKE_PEDAL].value = BrakeStates.RELEASED
        asserts.are_equal(vehicle_api.signals.get_all_signals(), signals)
