import pytest
from q_2818_applyOperationsToMaximizeScore import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([8, 3, 9, 3, 8], 2, 81), ([19, 12, 14, 6, 10, 18], 3, 4788)]
)
class TestSolution:
    def test_maximumScore(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumScore(
                nums,
                k,
            )
            == output
        )
