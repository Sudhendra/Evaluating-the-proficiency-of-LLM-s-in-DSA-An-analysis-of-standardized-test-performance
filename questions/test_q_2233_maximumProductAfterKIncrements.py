import pytest
from q_2233_maximumProductAfterKIncrements import Solution


@pytest.mark.parametrize("nums, k, output", [([0, 4], 5, 20), ([6, 3, 3, 2], 2, 216)])
class TestSolution:
    def test_maximumProduct(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumProduct(
                nums,
                k,
            )
            == output
        )
