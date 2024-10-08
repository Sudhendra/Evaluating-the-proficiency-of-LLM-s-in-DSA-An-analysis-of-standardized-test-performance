import pytest
from q_0137_singleNumberIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 2, 3, 2], 3), ([0, 1, 0, 1, 0, 1, 99], 99)]
)
class TestSolution:
    def test_singleNumber(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.singleNumber(
                nums,
            )
            == output
        )
