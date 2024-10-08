import pytest
from q_2042_checkIfNumbersAreAscendingInASentence import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("1 box has 3 blue 4 red 6 green and 12 yellow marbles", True),
        ("hello world 5 x 5", False),
        ("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s", False),
    ],
)
class TestSolution:
    def test_areNumbersAscending(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.areNumbersAscending(
                s,
            )
            == output
        )
