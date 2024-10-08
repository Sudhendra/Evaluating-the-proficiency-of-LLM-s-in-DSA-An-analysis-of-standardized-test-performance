import pytest
from q_2375_constructSmallestNumberFromDiString import Solution


@pytest.mark.parametrize(
    "pattern, output", [("IIIDIDDD", "123549876"), ("DDD", "4321")]
)
class TestSolution:
    def test_smallestNumber(self, pattern: str, output: str):
        sc = Solution()
        assert (
            sc.smallestNumber(
                pattern,
            )
            == output
        )
