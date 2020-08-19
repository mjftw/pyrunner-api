from .interfaces.irunner import IRunner


class PyRunner(IRunner):
    def run(self, code: str) -> str:
        return ''
