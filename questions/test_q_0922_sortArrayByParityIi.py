import pytest
from q_0922_sortArrayByParityIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 2, 5, 7], [4, 5, 2, 7]), ([2, 3], [2, 3])]
)
class TestSolution:
    def test_sortArrayByParityII(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortArrayByParityII(
                nums,
            )
            == output
        )
