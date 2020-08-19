from io import StringIO
from contextlib import redirect_stdout

from .interfaces.irunner import IRunner


class PyRunner(IRunner):
    def run(self, code: str) -> str:
        stdout = StringIO()
        with redirect_stdout(stdout):
            exec(code)

        return stdout.getvalue()
