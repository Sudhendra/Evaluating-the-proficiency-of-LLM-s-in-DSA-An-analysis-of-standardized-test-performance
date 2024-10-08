import pytest
from q_1913_maximumProductDifferenceBetweenTwoPairs import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 6, 2, 7, 4], 34), ([4, 2, 5, 9, 7, 4, 8], 64)]
)
class TestSolution:
    def test_maxProductDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProductDifference(
                nums,
            )
            == output
        )
