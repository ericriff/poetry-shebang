# poetry-shebang

*poetry-shebang* allows you to put scripts in your path that run in a poetry environment.

This solves the problem of launching `poetry run script.py` from outside the script directory.


## Credits

This project is based on *pipenv-shebang*. Take a look at this project [here](https://github.com/laktak/pipenv-shebang).

## Usage

Put this shebang at the top of your script:

```
#!/usr/bin/env poetry-shebang
```

You can also run your script with

```
poetry-shebang /path/to/script
```

## Installation

```
sudo pip install poetry-shebang

# or
pip install --user poetry-shebang
```
