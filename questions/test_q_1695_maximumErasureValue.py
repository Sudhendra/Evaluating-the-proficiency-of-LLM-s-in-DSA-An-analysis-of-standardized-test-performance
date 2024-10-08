import pytest
from q_1695_maximumErasureValue import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 2, 4, 5, 6], 17), ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8)]
)
class TestSolution:
    def test_maximumUniqueSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumUniqueSubarray(
                nums,
            )
            == output
        )
