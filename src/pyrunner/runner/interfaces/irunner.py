import abc

from ..runresult import RunResult


class IRunner(metaclass=abc.ABCMeta):
    '''Interface for code runners'''
    @abc.abstractmethod
    def run(self, code: str) -> RunResult:
        '''Run an independent piece of code and return the result

        Args:
            code (str): Code to be run
        Returns:
            RunResult: stdout and stdio resulting from running the code
        '''
