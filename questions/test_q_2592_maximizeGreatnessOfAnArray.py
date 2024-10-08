import pytest
from q_2592_maximizeGreatnessOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 5, 2, 1, 3, 1], 4), ([1, 2, 3, 4], 3)]
)
class TestSolution:
    def test_maximizeGreatness(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximizeGreatness(
                nums,
            )
            == output
        )
