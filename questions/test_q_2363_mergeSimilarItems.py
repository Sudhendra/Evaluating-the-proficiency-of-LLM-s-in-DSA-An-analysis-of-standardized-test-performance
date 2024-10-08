import pytest
from q_2363_mergeSimilarItems import Solution


@pytest.mark.parametrize(
    "items1, items2, output",
    [
        ([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]], [[1, 6], [3, 9], [4, 5]]),
        ([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]], [[1, 4], [2, 4], [3, 4]]),
        ([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]], [[1, 7], [2, 4], [7, 1]]),
    ],
)
class TestSolution:
    def test_mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.mergeSimilarItems(
                items1,
                items2,
            )
            == output
        )
