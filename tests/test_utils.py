from pyenv_poetry_tox_pytest_example import utils


def test_add():
    assert utils.add(1, 2) == 3


def test_print_greet(capfd):
    utils.print_greet()

    out, err = capfd.readouterr()
    assert out == 'Hello, world!\n'
    assert err == ''


def test_print_python_version(capfd):
    utils.print_python_version()

    out, err = capfd.readouterr()
    assert out != ''
    assert err == ''
