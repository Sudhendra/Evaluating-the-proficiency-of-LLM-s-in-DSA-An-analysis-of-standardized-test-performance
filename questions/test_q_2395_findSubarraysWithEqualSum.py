import pytest
from q_2395_findSubarraysWithEqualSum import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 2, 4], True), ([1, 2, 3, 4, 5], False), ([0, 0, 0], True)]
)
class TestSolution:
    def test_findSubarrays(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.findSubarrays(
                nums,
            )
            == output
        )
