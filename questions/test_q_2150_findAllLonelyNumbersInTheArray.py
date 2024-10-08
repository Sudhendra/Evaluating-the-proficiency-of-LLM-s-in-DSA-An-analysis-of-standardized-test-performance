import pytest
from q_2150_findAllLonelyNumbersInTheArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([10, 6, 5, 8], [10, 8]), ([1, 3, 5, 3], [1, 5])]
)
class TestSolution:
    def test_findLonely(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findLonely(
                nums,
            )
            == output
        )
