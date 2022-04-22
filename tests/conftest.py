import os

import pytest
from pytest import Parser

from project.configs import config
from project.consts.acc_pedal_states import AccPedalStates
from project.consts.battery_states import BatteryStates
from project.consts.gear_states import GearStates
from project.steps import vehicle_steps as steps
from project.test_clients.vehicle_api_clients import VehicleApi


@pytest.fixture(scope="session")
def vehicle_api(request: pytest.FixtureRequest) -> VehicleApi:
    base_url = request.config.getoption("--base_url") or os.getenv("BASE_URL") or config.BASE_URL
    return VehicleApi(base_url)


@pytest.fixture(autouse=True)
def default_state(vehicle_api: VehicleApi) -> None:
    steps.set_battery_state(vehicle_api, BatteryStates.READY)
    steps.set_acc_pedal_pos(vehicle_api, AccPedalStates.POS_0)
    steps.press_brake(vehicle_api)
    steps.select_gear(vehicle_api, GearStates.PARK)


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--base_url', help='Vehicle api base url', default=None)
