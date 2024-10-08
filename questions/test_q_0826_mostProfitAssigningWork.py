import pytest
from q_0826_mostProfitAssigningWork import Solution


@pytest.mark.parametrize(
    "difficulty, profit, worker, output",
    [
        ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
        ([85, 47, 57], [24, 66, 99], [40, 25, 25], 0),
    ],
)
class TestSolution:
    def test_maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maxProfitAssignment(
                difficulty,
                profit,
                worker,
            )
            == output
        )
