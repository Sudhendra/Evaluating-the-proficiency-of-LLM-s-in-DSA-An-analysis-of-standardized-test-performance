import pytest
from q_2149_rearrangeArrayElementsBySign import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]), ([-1, 1], [1, -1])]
)
class TestSolution:
    def test_rearrangeArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.rearrangeArray(
                nums,
            )
            == output
        )
