import allure
import pytest_check as check


@allure.step('Assert are equal: "{actual}" - "{expected}"')
def are_equal(actual, expected):
    """
    Compares 2 values of any type.

    Args:
        actual: Actual value
        expected: Expected value

    Raises:
        AssertionError: If 'actual' is not equal to 'expected'
    """
    assert actual == expected, "Actual result does not match with expected.\n" \
                               f"Expected: {expected}.\n" \
                               f"Actual: {actual}."


@allure.step('Soft assert are equal: "{actual}" - "{expected}"')
def are_equal_soft(actual, expected):
    """
    Compares 2 values of any type and continue without interruption.

    Args:
        actual: Actual value
        expected: Expected value

    Raises:
        AssertionError: If 'actual' is not equal to 'expected'
    """
    check.equal(actual, expected, "Actual result does not match with expected.\n"
                                  f"Expected: {expected}.\n"
                                  f"Actual: {actual}.")
