import pytest
from q_2974_minimumNumberGame import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 4, 2, 3], [3, 2, 5, 4]), ([2, 5], [5, 2])]
)
class TestSolution:
    def test_numberGame(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.numberGame(
                nums,
            )
            == output
        )
