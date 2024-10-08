import pytest
from q_2262_totalAppealOfAString import Solution


@pytest.mark.parametrize("s, output", [("abbca", 28), ("code", 20)])
class TestSolution:
    def test_appealSum(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.appealSum(
                s,
            )
            == output
        )
