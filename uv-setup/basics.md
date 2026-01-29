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

uv.lock similar to json.lock but you do push it to github
uv remove package.name: removes dependency

•• If Using Tensorflow or other dependency that cannot be installed because the version of python you're using is too modern you will get the following error: Mo solution found when resolving dependencies:

just downgrade the version of python you're using to the required one according to tensorflow.

running `uv lock` will generate a new lock file

Learn --lib --app for uv init... we will be using --app a lot when creating applications.

 -->