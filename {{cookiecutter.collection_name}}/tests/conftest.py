import pytest
from nebula.testing.utilities import nebula_test_harness


@pytest.fixture(scope="session", autouse=True)
def nebula_db():
    """
    Sets up test harness for temporary DB during test runs.
    """
    with nebula_test_harness():
        yield


@pytest.fixture(autouse=True)
def reset_object_registry():
    """
    Ensures each test has a clean object registry.
    """
    from nebula.context import NebulaObjectRegistry

    with NebulaObjectRegistry():
        yield
