import pytest
from q_1608_specialArrayWithXElementsGreaterThanOrEqualX import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 5], 2), ([0, 0], -1), ([0, 4, 3, 0, 4], 3)]
)
class TestSolution:
    def test_specialArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.specialArray(
                nums,
            )
            == output
        )
