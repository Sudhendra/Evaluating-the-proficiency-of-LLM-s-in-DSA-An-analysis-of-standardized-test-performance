import pytest
from q_0448_findAllNumbersDisappearedInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]), ([1, 1], [2])]
)
class TestSolution:
    def test_findDisappearedNumbers(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findDisappearedNumbers(
                nums,
            )
            == output
        )
