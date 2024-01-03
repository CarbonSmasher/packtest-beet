import click
from beet import Project
from beet.toolchain.cli import beet

pass_project = click.make_pass_decorator(Project)  # type: ignore


@beet.command()
@pass_project
def test(project: Project):
    """Run PackTest tests"""
    print("PACKTEST")