import pytest
from q_0229_majorityElementIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 2, 3], [3]), ([1], [1]), ([1, 2], [1, 2])]
)
class TestSolution:
    def test_majorityElement(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.majorityElement(
                nums,
            )
            == output
        )
