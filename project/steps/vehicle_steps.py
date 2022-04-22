import allure

from project.consts.acc_pedal_states import AccPedalStates
from project.consts.battery_states import BatteryStates
from project.consts.brake_pedal_states import BrakeStates
from project.consts.gear_states import GearStates
from project.consts.pin_id import PinId
from project.models.pin import Pin
from project.test_clients.vehicle_api_clients import VehicleApi


@allure.step('Stop vehicle and select gear: "{gear}"')
def stop_vehicle_and_select_gear(client: VehicleApi, gear: str) -> None:
    set_acc_pedal_pos(client, AccPedalStates.POS_0)
    press_brake(client)
    select_gear(client, gear)
    release_brake(client)


@allure.step('Select gear: "{gear}"')
def select_gear(client: VehicleApi, gear: str) -> None:
    voltages = GearStates.get_voltages(gear)
    pin1 = Pin(PinId.GEAR_1, voltages[0])
    pin2 = Pin(PinId.GEAR_2, voltages[1])
    client.pins.update_pins(pin1, pin2)


@allure.step('Press brake')
def press_brake(client: VehicleApi) -> None:
    set_brake_state(client, BrakeStates.PRESSED)


@allure.step('Release brake')
def release_brake(client: VehicleApi) -> None:
    set_brake_state(client, BrakeStates.RELEASED)


@allure.step('Set acc pedal position: "{position}"')
def set_acc_pedal_pos(client: VehicleApi, position: str) -> None:
    voltage = AccPedalStates.get_voltage(position)
    client.pins.update_pin(PinId.ACC_PEDAL, voltage)


@allure.step('Set battery state: "{state}"')
def set_battery_state(client: VehicleApi, state: str) -> None:
    voltage = BatteryStates.get_voltage(state)
    client.pins.update_pin(PinId.BATTERY_VOLTAGE, voltage)


@allure.step('Set brake state: "{state}"')
def set_brake_state(client: VehicleApi, state: str) -> None:
    voltage = BrakeStates.get_voltage(state)
    client.pins.update_pin(PinId.BRAKE_PEDAL, voltage)
