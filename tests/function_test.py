import re

import pytest

from gh_action_test import add_values
from gh_action_test import main


@pytest.mark.parametrize(
    ('a', 'b', 'res'),
    (
        (2, 3, 5),
        (3, 4, 7),
        (4, 5, 9),
        (5, 6, 11),
        (6, 7, 13),
    ),
)
def test_add_values(a, b, res):
    assert add_values(a, b) == res


def test_main_fun(capsys):
    main()
    captured = capsys.readouterr()
    pattern = re.compile(
        r'hello world, at 20[2-9][0-9]-(0[1-9]|1[0-2])-'
        r'(0[1-9]|1[0-9]|2[0-9]|3[0-1]) (0[0-9]|1[0-9]|2[0-3])'
        r'(:[0-5][0-9]){2}.\d{6}',
    )
    assert re.match(pattern, captured.out)
