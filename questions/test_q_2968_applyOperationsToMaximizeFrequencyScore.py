import pytest
from q_2968_applyOperationsToMaximizeFrequencyScore import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 6, 4], 3, 3), ([1, 4, 4, 2, 4], 0, 3)]
)
class TestSolution:
    def test_maxFrequencyScore(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxFrequencyScore(
                nums,
                k,
            )
            == output
        )
