import pytest
from q_2100_findGoodDaysToRobTheBank import Solution


@pytest.mark.parametrize(
    "security, time, output",
    [
        ([5, 3, 3, 3, 5, 6, 2], 2, [2, 3]),
        ([1, 1, 1, 1, 1], 0, [0, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6], 2, []),
    ],
)
class TestSolution:
    def test_goodDaysToRobBank(self, security: List[int], time: int, output: List[int]):
        sc = Solution()
        assert (
            sc.goodDaysToRobBank(
                security,
                time,
            )
            == output
        )
