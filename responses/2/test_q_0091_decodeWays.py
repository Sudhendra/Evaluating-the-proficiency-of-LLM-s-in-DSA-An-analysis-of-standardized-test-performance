import pytest
from q_0091_decodeWays import Solution


@pytest.mark.parametrize("s, output", [("12", 2), ("226", 3), ("06", 0)])
class TestSolution:
    def test_numDecodings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numDecodings(
                s,
            )
            == output
        )
