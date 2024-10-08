import pytest
from q_2049_countNodesWithTheHighestScore import Solution


@pytest.mark.parametrize("parents, output", [([-1, 2, 0, 2, 0], 3), ([-1, 2, 0], 2)])
class TestSolution:
    def test_countHighestScoreNodes(self, parents: List[int], output: int):
        sc = Solution()
        assert (
            sc.countHighestScoreNodes(
                parents,
            )
            == output
        )
