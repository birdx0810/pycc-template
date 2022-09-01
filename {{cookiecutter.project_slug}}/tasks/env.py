from invoke import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx):
    """Remove virtual environment"""
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx, e="dev"):
    """Install virtual environment (default: dev)"""
    if e.startswith("prod"):
        ctx.run("pipenv install --deploy")
    else:
        ctx.run("pipenv install --dev")
        ctx.run("git init")
        {% if cookiecutter.git_origin != "" -%}
        ctx.run("git remote set-url origin {% cookiecutter.git_origin %}")
        {%- endif %}
        ctx.run(f"{VENV_PREFIX} pre-commit install -t pre-commit")
        ctx.run(f"{VENV_PREFIX} pre-commit install -t pre-push")
        ctx.run(f"{VENV_PREFIX} pre-commit install -t commit-msg")
        ctx.run(f"{VENV_PREFIX} pre-commit autoupdate")
