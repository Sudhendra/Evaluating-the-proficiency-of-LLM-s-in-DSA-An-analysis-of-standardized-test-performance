import pytest
from q_1207_uniqueNumberOfOccurrences import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ],
)
class TestSolution:
    def test_uniqueOccurrences(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.uniqueOccurrences(
                arr,
            )
            == output
        )
