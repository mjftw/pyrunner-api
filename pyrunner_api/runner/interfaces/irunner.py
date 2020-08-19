import abc


class IRunner(metaclass=abc.ABCMeta):
    ''' Interface for code runners '''
    @abc.abstractmethod
    def run(self, code: str) -> str:
        ''' Run an independent piece of code and return the stdout output'''
        pass
