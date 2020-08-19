from unittest import TestCase

from pyrunner_api.runner.pyrunner import PyRunner


class PyRunnerTest(TestCase):
    def setUp(self):
        self.runner = PyRunner()

    def test_run_returns_str(self):
        source = '#'
        output = self.runner.run(source)
        self.assertIsInstance(output, str)

    def test_run_handles_stdout_from_single_code_line(self):
        source = r'print("Hello World!")'
        output = self.runner.run(source)
        self.assertEqual('Hello World!\n', output)
