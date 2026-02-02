To setup python virtual environment:
python3 -m venv name:(.venv)

acivate environment MAC:

<!-- When you create the .venv file it creates this bin/activate file so when you run the virtual environment you're running this file. 

After activation if you look in the activate file under bin there are other functions you can run. They don't have to be ran by using source, you can simply call the function by name thats it. So, for deactive in the command line you run `(.venv) rilla@MacBook-Pro % deactivate`. -->
source .venv/bin/activate

<!-- The importance of virtual environments with .venv is that it gives your application a virtual environment where all variables, applications modules, and everything pertaining to this individual python project is placed. Think about it like node_modules combined with a .env for this project specifically. 

To run module installs then you can utilize pip install and module identifier by name. For instance, pip install flask. 

Alternatively, you can setup a file with project dependencies and call each by name in there. Have a look at dependencies.txt. 

to run: pip install -r filename.txt. In our instance, pip install -r dependencies.txt
To install specific versions within dependencies.txt you can use ==0.0.0 to install specific versions. Example, requests==2.31.0. -->

