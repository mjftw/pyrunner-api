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

    def test_run_handles_stdout_from_multiple_code_lines(self):
        source = ('print("Foo")\n'
                  'print("Bar")\n')
        output = self.runner.run(source)
        self.assertEqual('Foo\nBar\n', output)

    def test_run_should_give_no_output_on_empty_code(self):
        self.assertEqual('', self.runner.run(''))

    def test_run_should_give_no_output_on_only_comments(self):
        self.assertEqual('', self.runner.run('#\n#'))
