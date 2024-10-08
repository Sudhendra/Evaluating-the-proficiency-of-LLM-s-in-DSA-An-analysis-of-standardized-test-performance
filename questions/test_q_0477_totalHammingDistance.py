import pytest
from q_0477_totalHammingDistance import Solution


@pytest.mark.parametrize("nums, output", [([4, 14, 2], 6), ([4, 14, 4], 4)])
class TestSolution:
    def test_totalHammingDistance(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.totalHammingDistance(
                nums,
            )
            == output
        )
