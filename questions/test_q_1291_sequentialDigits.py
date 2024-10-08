import pytest
from q_1291_sequentialDigits import Solution


@pytest.mark.parametrize(
    "low, high, output",
    [
        (100, 300, [123, 234]),
        (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
    ],
)
class TestSolution:
    def test_sequentialDigits(self, low: int, high: int, output: List[int]):
        sc = Solution()
        assert (
            sc.sequentialDigits(
                low,
                high,
            )
            == output
        )
