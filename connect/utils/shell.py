from subprocess import PIPE, Popen
from typing import Tuple


class RunCommand:
    def __init__(self, cmd: str):
        self.cmd = cmd
        if self.cmd is None:
            raise ValueError("No command found error")

    def execute(self) -> Tuple[str, str, int]:
        cmd_list = self.cmd.split(" ")
        result = Popen(
            cmd_list, stderr=PIPE, stdout=PIPE
        )
        output, err_output = result.communicate()
        return output.decode("utf-8"), err_output.decode("utf-8"), result.returncode
