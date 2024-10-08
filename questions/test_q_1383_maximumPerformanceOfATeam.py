import pytest
from q_1383_maximumPerformanceOfATeam import Solution


@pytest.mark.parametrize(
    "n, speed, efficiency, k, output",
    [
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
    ],
)
class TestSolution:
    def test_maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxPerformance(
                n,
                speed,
                efficiency,
                k,
            )
            == output
        )
