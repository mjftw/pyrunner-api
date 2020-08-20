from io import StringIO
from contextlib import redirect_stderr, redirect_stdout
from traceback import print_exc

from .interfaces.irunner import IRunner
from .runresult import RunResult


class PyRunner(IRunner):
    def run(self, code: str) -> RunResult:
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stdout(stdout):
            with redirect_stderr(stderr):
                try:
                    exec(code)
                except Exception:
                    print_exc()

        return RunResult(stdout.getvalue(), stderr.getvalue())
