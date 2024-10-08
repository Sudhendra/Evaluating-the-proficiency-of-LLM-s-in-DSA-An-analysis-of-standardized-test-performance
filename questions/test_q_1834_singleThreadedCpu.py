import pytest
from q_1834_singleThreadedCpu import Solution


@pytest.mark.parametrize(
    "tasks, output",
    [
        ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
        ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
    ],
)
class TestSolution:
    def test_getOrder(self, tasks: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.getOrder(
                tasks,
            )
            == output
        )
