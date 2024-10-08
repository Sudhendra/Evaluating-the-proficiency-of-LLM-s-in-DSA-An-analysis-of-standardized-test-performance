import pytest
from q_0466_countTheRepetitions import Solution


@pytest.mark.parametrize(
    "s1, n1, s2, n2, output", [("acb", 4, "ab", 2, 2), ("acb", 1, "acb", 1, 1)]
)
class TestSolution:
    def test_getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int, output: int):
        sc = Solution()
        assert (
            sc.getMaxRepetitions(
                s1,
                n1,
                s2,
                n2,
            )
            == output
        )
