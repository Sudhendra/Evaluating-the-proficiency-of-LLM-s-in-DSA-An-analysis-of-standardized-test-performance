import pytest
from q_2315_countAsterisks import Solution


@pytest.mark.parametrize(
    "s, output",
    [("l|*e*et|c**o|*de|", 2), ("iamprogrammer", 0), ("yo|uar|e**|b|e***au|tifu|l", 5)],
)
class TestSolution:
    def test_countAsterisks(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countAsterisks(
                s,
            )
            == output
        )
