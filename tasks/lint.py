from invoke import task

from tasks.common import COMMON_TARGETS, VENV_PREFIX


@task
def isort(ctx):
    """Run isort import sorter"""
    print("***Running isort***")
    ctx.run(f"{VENV_PREFIX} isort --atomic {COMMON_TARGETS}")
    print("***Finished isort***\n")


@task
def black(ctx):
    """Run black code styler"""
    print("***Running black***")
    ctx.run(f"{VENV_PREFIX} black {COMMON_TARGETS}")
    print("***Finished black***\n")


@task
def flake8(ctx):
    """Run flake8 linter"""
    print("***Running flake8***")
    ctx.run(f"{VENV_PREFIX} flake8 --config=setup.cfg")
    print("***Finished flake8***\n")


@task
def mypy(ctx):
    """Run mypy static typing"""
    print("***Running mypy***")
    ctx.run(f"{VENV_PREFIX} mypy")
    print("***Finished mypy***\n")


@task(pre=[isort, black, flake8, mypy])
def all(ctx):
    """Run all linting tools"""
    pass
