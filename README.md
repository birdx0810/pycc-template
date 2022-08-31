# pycc-template

This is my personal Cookiecutter template for my Python projects.

## Features
- Virtual Environment Manager: `pipenv`
- Coding Style
    - Import sorter: `isort`
    - Auto-formatter: `black`
    - Linter: `flake8`
    - Static Typing: `mypy`
- Test: `pytest`
- Version Manager
    - Conventional commits: `commitizen`
    - Git commit hooks: `pre-commit`
- Tool Organizer: `invoke`

## Getting Started

Pyenv Python Version Manager.
```sh
# Pyenv
curl https://pyenv.run | bash
## For bash
# export PYENV_ROOT="$HOME/.pyenv"
# command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
# eval "$(pyenv init -)"
## For fish
# omf install pyenv

pyenv install <VERSION>
pyenv global <VERSION>
```

Environment Tools
```sh
# Pipx for installing Python-based CLI tools
python3 -m pip install --user pipx
pipx install pipenv
pipx install cookiecutter
pipx install commitizen
pipx install invoke
```

Development Tools
```sh
# Install tools
pipenv install black isort flake8 mypy pytest --dev
```
