from unittest import TestCase

from pyrunner_api.runner.pyrunner import PyRunner


class PyRunnerTest(TestCase):
    def setUp(self):
        self.runner = PyRunner()

    def test_run_returns_str(self):
        source = '#'
        output = self.runner.run(source)
        self.assertIsInstance(output, str)