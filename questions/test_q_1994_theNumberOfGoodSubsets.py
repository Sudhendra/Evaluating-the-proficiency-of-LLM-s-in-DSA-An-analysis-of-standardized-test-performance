import pytest
from q_1994_theNumberOfGoodSubsets import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3, 4], 6), ([4, 2, 3, 15], 5)])
class TestSolution:
    def test_numberOfGoodSubsets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfGoodSubsets(
                nums,
            )
            == output
        )
