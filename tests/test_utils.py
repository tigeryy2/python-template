import tempfile
from pathlib import Path

import pytest

from python_template.utils.utils import change_dir


def test_change_dir_succeeds():
    original_dir = Path.cwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir).resolve()
        with change_dir(temp_dir):
            assert Path.cwd() == temp_dir
        # Ensure we returned to the original directory
        assert Path.cwd() == original_dir


def test_change_dir_handles_exception():
    original_dir = Path.cwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(Exception) as exc_info:
            with change_dir(Path(temp_dir)):
                # Ensure the directory was changed
                assert Path.cwd() == Path(temp_dir)
                # Raise an exception to trigger the finally

    # Ensure we returned to the original directory
    assert Path.cwd() == original_dir