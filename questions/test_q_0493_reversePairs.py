import pytest
from q_0493_reversePairs import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 2, 3, 1], 2), ([2, 4, 3, 5, 1], 3)])
class TestSolution:
    def test_reversePairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.reversePairs(
                nums,
            )
            == output
        )
