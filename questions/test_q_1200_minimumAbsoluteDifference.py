import pytest
from q_1200_minimumAbsoluteDifference import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ([1, 3, 6, 10, 15], [[1, 3]]),
        ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]),
    ],
)
class TestSolution:
    def test_minimumAbsDifference(self, arr: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.minimumAbsDifference(
                arr,
            )
            == output
        )
