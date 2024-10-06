`poetry install` \
pip install pipx \
pipx install poetry \
pipx upgrade poetry \
pipx uninstall poetry

`new project` \
poetry new poetry-demo1

`set up venv` \
python -m venv .venv 
.venv\scripts\activate

`file pyproject.toml - configuration` \
`adding dependiancies` \
$ poetry add pandas \
$ poetry add pendulum

etc.

`initiate project based on poetry init` \
mkdir <--NewFolder--> \
cd <--NewFolder--> \
poetry init


`[build-system] exists, run to install dependencies` \
pip install -e .

`Install only dependencies`
poetry install --no-root


`Install / unsitall packages` \
pip install <--package name--> / or use poetry \
pip uninstall <--package name-->