<!-- uv works on python 3.7 and up

UV DOCS: https://docs.astral.sh/uv/getting-started/installation/

Running Scripts: uv run name

install python version: uv install version (can grab from list)
view python list: uv python list

install modules & dependencies:

make run with dependencies (ideal for python scripts not for project applications):
uv init --script main.py --python 3.14
This will insert the following in the file specified:
# /// script
# requires-python = ">=3.14"
# dependencies = ["requests"]
# ///
all project dependencies should be listed in the dependencies array. Or, you can allow uv to handle it by running: uv add --script main.py "dependency-name"

Make run with dependencies for PROJECTS:
from within the root file (in this example: project-example) run:
uv init:
    This will create a few files automatically including: .python-version, main.py, pyproject.toml, readme, 

upon running it'll run the .venv for you automatically and install needed dependencies. 

 -->