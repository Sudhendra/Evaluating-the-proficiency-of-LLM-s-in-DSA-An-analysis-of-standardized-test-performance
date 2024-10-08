import pytest
from q_0047_permutationsIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 1, 2], None),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ],
)
class TestSolution:
    def test_permuteUnique(self, nums: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.permuteUnique(
                nums,
            )
            == output
        )
