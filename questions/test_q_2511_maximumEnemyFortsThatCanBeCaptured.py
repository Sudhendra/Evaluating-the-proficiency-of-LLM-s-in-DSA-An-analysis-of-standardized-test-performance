import pytest
from q_2511_maximumEnemyFortsThatCanBeCaptured import Solution


@pytest.mark.parametrize(
    "forts, output", [([1, 0, 0, -1, 0, 0, 0, 0, 1], 4), ([0, 0, 1, -1], 0)]
)
class TestSolution:
    def test_captureForts(self, forts: List[int], output: int):
        sc = Solution()
        assert (
            sc.captureForts(
                forts,
            )
            == output
        )
