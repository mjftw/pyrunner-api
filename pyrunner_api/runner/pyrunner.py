from io import StringIO
from contextlib import redirect_stdout

from .interfaces.irunner import IRunner
from .runresult import RunResult


class PyRunner(IRunner):
    def run(self, code: str) -> RunResult:
        stdout = StringIO()
        with redirect_stdout(stdout):
            exec(code)

        return RunResult(stdout.getvalue(), '')
