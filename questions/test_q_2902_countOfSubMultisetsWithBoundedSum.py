import pytest
from q_2902_countOfSubMultisetsWithBoundedSum import Solution


@pytest.mark.parametrize(
    "nums, l, r, output",
    [
        ([1, 2, 2, 3], 6, 6, 1),
        ([2, 1, 4, 2, 7], 1, 5, 7),
        ([1, 2, 1, 3, 5, 2], 3, 5, 9),
    ],
)
class TestSolution:
    def test_countSubMultisets(self, nums: List[int], l: int, r: int, output: int):
        sc = Solution()
        assert (
            sc.countSubMultisets(
                nums,
                l,
                r,
            )
            == output
        )
