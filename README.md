# ArtifyAPI Documentation
API for the Artify Project


## Installing python 

firstly you must set a correct version of python on your machine 
we use a pyenv module to do this.

for linux

```
pip install pyenv 
``` 
for Windows

```
pip install pyenv-win
```
install correct vesion of python

```
pyenv install 3.8.6
```

## Copy repo from github

you must create folder on your machine and open there `cmd`, `powershell`,`bash`, or simple linux `terminal`
create a virtual eviroment by module pipenv or open a PyCharm on this folder and in venv options select pipenv.
and execute comand

```
https://github.com/stepan9773/Artify.git
```

then update a requirements by execute setup.py, then
```
pipenv update 
```
and pipenv must automaticaly start installing all dependencies for project 

and finaly start a project app by command 
```
python manage.py
```

## How use
On console you will see a HTTP path, execute it on browser and add to him `/smoke`.

You will see text messege `Hello` on browser tab.