import pytest
from q_0693_binaryNumberWithAlternatingBits import Solution


@pytest.mark.parametrize("n, output", [(5, True), (7, False), (11, False)])
class TestSolution:
    def test_hasAlternatingBits(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.hasAlternatingBits(
                n,
            )
            == output
        )
