import pytest
from q_1461_checkIfAStringContainsAllBinaryCodesOfSizeK import Solution


@pytest.mark.parametrize(
    "s, k, output", [("00110110", 2, True), ("0110", 1, True), ("0110", 2, False)]
)
class TestSolution:
    def test_hasAllCodes(self, s: str, k: int, output: bool):
        sc = Solution()
        assert (
            sc.hasAllCodes(
                s,
                k,
            )
            == output
        )
