import pytest
from q_0857_minimumCostToHireKWorkers import Solution


@pytest.mark.parametrize(
    "quality, wage, k, output",
    [
        ([10, 20, 5], [70, 50, 30], 2, 105.0),
        ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.66667),
    ],
)
class TestSolution:
    def test_mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int, output: float
    ):
        sc = Solution()
        assert (
            sc.mincostToHireWorkers(
                quality,
                wage,
                k,
            )
            == output
        )
