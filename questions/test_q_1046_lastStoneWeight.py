import pytest
from q_1046_lastStoneWeight import Solution


@pytest.mark.parametrize("stones, output", [([2, 7, 4, 1, 8, 1], 1), ([1], 1)])
class TestSolution:
    def test_lastStoneWeight(self, stones: List[int], output: int):
        sc = Solution()
        assert (
            sc.lastStoneWeight(
                stones,
            )
            == output
        )
