import pytest
from q_2454_nextGreaterElementIv import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 4, 0, 9, 6], [9, 6, 6, -1, -1]), ([3, 3], [-1, -1])]
)
class TestSolution:
    def test_secondGreaterElement(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.secondGreaterElement(
                nums,
            )
            == output
        )
