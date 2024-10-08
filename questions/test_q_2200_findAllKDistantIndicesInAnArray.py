import pytest
from q_2200_findAllKDistantIndicesInAnArray import Solution


@pytest.mark.parametrize(
    "nums, key, k, output",
    [
        ([3, 4, 9, 1, 3, 9, 5], 9, 1, [1, 2, 3, 4, 5, 6]),
        ([2, 2, 2, 2, 2], 2, 2, [0, 1, 2, 3, 4]),
    ],
)
class TestSolution:
    def test_findKDistantIndices(
        self, nums: List[int], key: int, k: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findKDistantIndices(
                nums,
                key,
                k,
            )
            == output
        )
