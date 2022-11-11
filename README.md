# pycc-template

This is a Cookiecutter template for Python projects.

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

For developing this template.

### Requirements

- Python
- pipenv
- pipx (recommended)

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

### Sidenote
To enable pre-commit on repositories, run the commands below before creating project to automatically run `pre-commit install`.
Add the `--allow-missing-config` flag to skip running `pre-commit install` if `.pre-commit-config.yaml` is not found.

```
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template [--allow-missing-config]
```

Reference: [pre-commit](https://pre-commit.com/#automatically-enabling-pre-commit-on-repositories)

## Author

[Daniel Tan](https://github.com/birdx0810) <birdx0810@gmail.com>
