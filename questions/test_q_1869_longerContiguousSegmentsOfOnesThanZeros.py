import pytest
from q_1869_longerContiguousSegmentsOfOnesThanZeros import Solution


@pytest.mark.parametrize(
    "s, output", [("1101", True), ("111000", False), ("110100010", False)]
)
class TestSolution:
    def test_checkZeroOnes(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkZeroOnes(
                s,
            )
            == output
        )
