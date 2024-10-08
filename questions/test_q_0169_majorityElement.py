import pytest
from q_0169_majorityElement import Solution


@pytest.mark.parametrize("nums, output", [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)])
class TestSolution:
    def test_majorityElement(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.majorityElement(
                nums,
            )
            == output
        )
