import pytest
from q_2601_primeSubtractionOperation import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 9, 6, 10], True), ([6, 8, 11, 12], True), ([5, 8, 3], False)]
)
class TestSolution:
    def test_primeSubOperation(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.primeSubOperation(
                nums,
            )
            == output
        )
