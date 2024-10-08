import pytest
from q_0164_maximumGap import Solution


@pytest.mark.parametrize("nums, output", [([3, 6, 9, 1], 3), ([10], 0)])
class TestSolution:
    def test_maximumGap(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumGap(
                nums,
            )
            == output
        )
