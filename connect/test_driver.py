from typer.testing import CliRunner
from connect.driver import app

runner = CliRunner()


def test_connect():
    runner.invoke(app, ["connect", "--config", ""])


def test_disconnect():
    runner.invoke(app, ["disconnect"])


def test_status():
    runner.invoke(app, ["status"])


if __name__ == '__main__':
    test_status()
