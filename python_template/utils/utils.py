"""
General Utilities
"""

import os
from contextlib import contextmanager
from pathlib import Path

from python_template.utils.loggable import Loggable


@contextmanager
def change_dir(new_dir: Path):
    """
    Changes the current working directory to the specified directory, then changes it back to the original directory.
    """
    original_dir = Path.cwd()
    Loggable.log().debug(
        f"Original directory is '{original_dir}', changing to '{new_dir}'"
    )
    try:
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(original_dir)
        Loggable.log().debug("Reverted to original directory")
