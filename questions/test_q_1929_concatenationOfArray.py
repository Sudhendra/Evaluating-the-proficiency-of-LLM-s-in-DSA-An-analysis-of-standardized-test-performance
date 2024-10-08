import pytest
from q_1929_concatenationOfArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 1], [1, 2, 1, 1, 2, 1]), ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])],
)
class TestSolution:
    def test_getConcatenation(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.getConcatenation(
                nums,
            )
            == output
        )
