import pytest
from q_0260_singleNumberIii import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 1, 3, 2, 5], [3, 5]), ([-1, 0], [-1, 0]), ([0, 1], [1, 0])]
)
class TestSolution:
    def test_singleNumber(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.singleNumber(
                nums,
            )
            == output
        )
