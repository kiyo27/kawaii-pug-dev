import importlib
import click
from collections import OrderedDict


_CLI_COMMANDS_PACKAGES = [
    'commands.create'
]


class BaseCommand(click.MultiCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cmd_packages = _CLI_COMMANDS_PACKAGES
        self._commands = {}
        self._commands = BaseCommand._set_commands(cmd_packages)

    @staticmethod
    def _set_commands(package_names):
        commands = OrderedDict()
        for pkg_name in package_names:
            cmd_name = pkg_name.split(".")[-1]
            commands[cmd_name] = pkg_name

        return commands

    def list_commands(self, ctx):
        return list(self._commands.keys())

    def get_command(self, ctx, cmd_name):
        if cmd_name not in self._commands:
            return None

        pkg_name = self._commands[cmd_name]

        try:
            mod = importlib.import_module(pkg_name)
        except ImportError:
            click.echo("Command not found.")
            return None

        if not hasattr(mod, "cli"):
            click.echo("Command is not configured correctly.")
            return None

        return mod.cli
