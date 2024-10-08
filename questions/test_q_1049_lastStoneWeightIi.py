import pytest
from q_1049_lastStoneWeightIi import Solution


@pytest.mark.parametrize(
    "stones, output", [([2, 7, 4, 1, 8, 1], 1), ([31, 26, 33, 21, 40], 5)]
)
class TestSolution:
    def test_lastStoneWeightII(self, stones: List[int], output: int):
        sc = Solution()
        assert (
            sc.lastStoneWeightII(
                stones,
            )
            == output
        )
