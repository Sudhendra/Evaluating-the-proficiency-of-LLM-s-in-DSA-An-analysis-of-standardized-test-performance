import pytest
from q_2779_maximumBeautyOfAnArrayAfterApplyingOperation import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([4, 6, 1, 2], 2, 3), ([1, 1, 1, 1], 10, 4)]
)
class TestSolution:
    def test_maximumBeauty(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumBeauty(
                nums,
                k,
            )
            == output
        )
