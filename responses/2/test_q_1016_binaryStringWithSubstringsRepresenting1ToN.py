import pytest
from q_1016_binaryStringWithSubstringsRepresenting1ToN import Solution


@pytest.mark.parametrize("s, n, output", [("0110", 3, True), ("0110", 4, False)])
class TestSolution:
    def test_queryString(self, s: str, n: int, output: bool):
        sc = Solution()
        assert (
            sc.queryString(
                s,
                n,
            )
            == output
        )
