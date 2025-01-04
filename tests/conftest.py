import pytest

from logs import LOGS_DIR
from python_template.utils.loggable import Loggable


@pytest.fixture(scope="session")
def logger():
    Loggable.setup_logs(log_path=LOGS_DIR / "tests.log")