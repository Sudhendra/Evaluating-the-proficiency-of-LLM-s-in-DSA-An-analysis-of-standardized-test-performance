import pytest
from q_2293_minMaxGame import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 5, 2, 4, 8, 2, 2], 1), ([3], 3)])
class TestSolution:
    def test_minMaxGame(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minMaxGame(
                nums,
            )
            == output
        )
