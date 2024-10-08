import pytest
from q_2527_findXorBeautyOfArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 4], 5), ([15, 45, 20, 2, 34, 35, 5, 44, 32, 30], 34)]
)
class TestSolution:
    def test_xorBeauty(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.xorBeauty(
                nums,
            )
            == output
        )
