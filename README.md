# pycc-template

This is my personal Cookiecutter template for my Python projects.

## Features
- Python Version Manager: `pyenv`
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

For editing this project.

### Requirements

- Python (`python_ver == system`)
- pyenv (`python_ver == x.y.z`)
- pipenv
- pipx (recommended)

### Installation
```
git clone https://github.com/
pipenv install
```

## Usage

To create a Python project using this template.

```
cookiecutter gh:birdx0810/pycc-template

project_name: PyCC Template
project_slug: pycc-template
project_description: This is my personal Cookiecutter template for my Python projects.
author_name: Daniel Tan
author_email: birdx0810@gmail.com
git_id: birdx0810
git_server: https://github.com
git_origin: https://github.com/birdx0810/pycc-template
python_ver: 3.10
```

## Author

[Daniel Tan](https://github.com/birdx0810) <birdx0810@gmail.com>
