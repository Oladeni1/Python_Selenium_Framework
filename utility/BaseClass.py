
# This class is used to connect with "conftest.py" or other re-usable functions:
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    pass           # used to remove red line (error)


