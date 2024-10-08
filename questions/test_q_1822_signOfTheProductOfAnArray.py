import pytest
from q_1822_signOfTheProductOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([-1, -2, -3, -4, 3, 2, 1], 1), ([1, 5, 0, 2, -3], 0), ([-1, 1, -1, 1, -1], -1)],
)
class TestSolution:
    def test_arraySign(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.arraySign(
                nums,
            )
            == output
        )
