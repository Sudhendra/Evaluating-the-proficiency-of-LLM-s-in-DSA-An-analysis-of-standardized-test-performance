import pytest
from q_2090_kRadiusSubarrayAverages import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
        ([100000], 0, [100000]),
        ([8], 100000, [-1]),
    ],
)
class TestSolution:
    def test_getAverages(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.getAverages(
                nums,
                k,
            )
            == output
        )
