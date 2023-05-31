"""
Main role of driver.py file is to fetch the values from config file and supply it to magic.sh
Other than that it can check whether all values are supplied or not.
To be discussed more.
"""
import json

import typer
from connect.utils.shell import RunCommand

app = typer.Typer()
scripts_directory = __file__[: __file__.rindex("driver.py")] + "/scripts/"


@app.command()
def connect(
    group: int = typer.Option(..., help="0 for cloudera vpn and 1 for full tunnel", prompt=True)
):
    """
    Auto Connects to the VPN.
    """
    typer.echo(RunCommand(cmd=f"sh {scripts_directory}/magic.sh {group}").execute())


@app.command()
def status():
    """
    Gives you the status of VPN i.e connected or disconnected.
    """
    typer.echo(RunCommand(cmd=f"sh {scripts_directory}/status.sh").execute())


@app.command()
def disconnect():
    """
    disconnects from the VPN
    """
    typer.echo(RunCommand(cmd=f"sh {scripts_directory}/disconnect.sh").execute())


@app.command()
def get_otp():
    typer.echo(RunCommand(cmd=f"sh {scripts_directory}/otp.sh").execute()[0])


if __name__ == "__main__":
    app()
