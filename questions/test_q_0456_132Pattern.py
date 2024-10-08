import pytest
from q_0456_132Pattern import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], False), ([3, 1, 4, 2], True), ([-1, 3, 2, 0], True)]
)
class TestSolution:
    def test_find132pattern(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.find132pattern(
                nums,
            )
            == output
        )
