# python-template
Template repo for Python projects

## Setup
[uv](https://docs.astral.sh/uv/) and `pyproject.toml` are used for Python package setup and dependency management.

1. Clone the project using git
2. Create the venv: `uv sync`. This will create a virtual environment in the `.venv` directory, using python specified
   in the `.python-version` file.
   By default, this will include the `dev` dependencies.
3. Activate the venv: `source .venv/bin/activate` (Linux or MacOS)
4. Install the project in editable mode: `uv pip install -e .`

## Dependency Management

Dependencies are defined within `requirements.in` and `requirements-dev.in` files.
These are then compiled into `requirements.txt` and `requirements-dev.txt` files using `compile-reqs` command.

To add or update a dependency:
1. Add the package to the relevant `.in` file
2. Run `compile-reqs` (installed as project script) to compile the requirements files
3. Run `uv add -r requirements.txt` and/or `uv add -r requirements-dev.txt --dev`, to update the `pyproject.toml` file
   with the new dependencies.
4. Run `uv sync` to update the virtual environment with the new dependencies.

The complete list of installed packages can be shown using `uv tree`.