import pytest
from q_1250_checkIfItIsAGoodArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([12, 5, 7, 23], True), ([29, 6, 10], True), ([3, 6], False)]
)
class TestSolution:
    def test_isGoodArray(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isGoodArray(
                nums,
            )
            == output
        )
