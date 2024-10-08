import pytest
from q_0219_containsDuplicateIi import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 2, 3, 1], 3, True), ([1, 0, 1, 1], 1, True), ([1, 2, 3, 1, 2, 3], 2, False)],
)
class TestSolution:
    def test_containsNearbyDuplicate(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.containsNearbyDuplicate(
                nums,
                k,
            )
            == output
        )
