import pytest
from q_0905_sortArrayByParity import Solution


@pytest.mark.parametrize("nums, output", [([3, 1, 2, 4], [2, 4, 3, 1]), ([0], [0])])
class TestSolution:
    def test_sortArrayByParity(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortArrayByParity(
                nums,
            )
            == output
        )
