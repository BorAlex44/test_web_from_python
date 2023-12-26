import pytest

from check_site import check_command


def test_site(site):
    assert check_command(f'nikto -h {site} -ssl -Tuning 4', '0 error(s)')


if __name__ == '__main__':
    pytest.main(['-vv'])
