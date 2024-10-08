import pytest
from q_1696_jumpGameVi import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, -1, -2, 4, -7, 3], 2, 7),
        ([10, -5, -2, 4, 0, 3], 3, 17),
        ([1, -5, -20, 4, -1, 3, -6, -3], 2, 0),
    ],
)
class TestSolution:
    def test_maxResult(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxResult(
                nums,
                k,
            )
            == output
        )
