from pyrunner.runner.runresult import RunResult


def test_run_returns_RunResult(pyrunner):
    source = '#'
    result = pyrunner.run(source)
    assert isinstance(result, RunResult)


def test_run_handles_stdout_from_single_code_line(pyrunner):
    source = r'print("Hello World!")'
    result = pyrunner.run(source)
    assert 'Hello World!\n' == result.stdout


def test_run_handles_stdout_from_multiple_code_lines(pyrunner):
    source_lines = [
        'print("Foo")',
        'print("Bar")'
    ]
    result = pyrunner.run('\n'.join(source_lines))
    assert 'Foo\nBar\n' == result.stdout


def test_run_should_give_no_result_on_empty_code(pyrunner):
    result = pyrunner.run('')
    assert '' == result.stdout


def test_run_should_give_no_result_on_only_comments(pyrunner):
    result = pyrunner.run('#\n#')
    assert '' == result.stdout


def test_run_should_handle_package_imports(pyrunner):
    import platform
    source_lines = [
        'import platform',
        '',
        'print(platform.release())'
    ]
    result = pyrunner.run('\n'.join(source_lines))
    assert platform.release() + '\n' == result.stdout


def test_run_should_allow_defining_functions(pyrunner):
    source_lines = [
        'def foo(a: int, b: int) -> int:',
        '    return a + b',
        '',
        'print(foo(1, 2))'
    ]
    result = pyrunner.run('\n'.join(source_lines))
    assert '3\n' == result.stdout


def test_run_exceptions_should_be_caught(pyrunner):
    source = r'raise RuntimeError'
    # Success if no exception raised to fail test
    pyrunner.run(source)


def test_run_should_return_traceback_to_stderr_on_exception(pyrunner):
    source = r'raise RuntimeError("Foo Bar!")'
    result = pyrunner.run(source)
    assert 'Traceback (most recent call last):\n' in result.stderr
    assert ('File "<string>", line 1, in <module>\n'
            'RuntimeError: Foo Bar!\n') in result.stderr
