from unittest import TestCase

from pyrunner_api.runner.pyrunner import PyRunner
from pyrunner_api.runner.runresult import RunResult


class PyRunnerTest(TestCase):
    def setUp(self):
        self.runner = PyRunner()

    def test_run_returns_RunResult(self):
        source = '#'
        result = self.runner.run(source)
        self.assertIsInstance(result, RunResult)

    def test_run_handles_stdout_from_single_code_line(self):
        source = r'print("Hello World!")'
        result = self.runner.run(source)
        self.assertEqual('Hello World!\n', result.stdout)

    def test_run_handles_stdout_from_multiple_code_lines(self):
        source_lines = [
            'print("Foo")',
            'print("Bar")'
        ]
        result = self.runner.run('\n'.join(source_lines))
        self.assertEqual('Foo\nBar\n', result.stdout)

    def test_run_should_give_no_result_on_empty_code(self):
        result = self.runner.run('')
        self.assertEqual('', result.stdout)

    def test_run_should_give_no_result_on_only_comments(self):
        result = self.runner.run('#\n#')
        self.assertEqual('', result.stdout)

    def test_run_should_handle_package_imports(self):
        import platform
        source_lines = [
            'import platform',
            '',
            'print(platform.release())'
        ]
        result = self.runner.run('\n'.join(source_lines))
        self.assertEqual(platform.release() + '\n', result.stdout)

    def test_run_should_allow_defining_functions(self):
        source_lines = [
            'def foo(a: int, b: int) -> int:',
            '    return a + b',
            '',
            'print(foo(1, 2))'
        ]
        result = self.runner.run('\n'.join(source_lines))
        self.assertEqual('3\n', result.stdout)

    def test_run_exceptions_should_be_caught(self):
        source = r'raise RuntimeError'
        # Success if no exception raised to fail test
        self.runner.run(source)

    def test_run_should_return_traceback_to_stderr_on_exception(self):
        source = r'raise RuntimeError("Foo Bar!")'
        result = self.runner.run(source)
        self.assertIn('Traceback (most recent call last):\n', result.stderr)
        self.assertIn('File "<string>", line 1, in <module>\n'
                      'RuntimeError: Foo Bar!\n', result.stderr)
