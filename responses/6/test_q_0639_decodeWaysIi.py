import pytest
from q_0639_decodeWaysIi import Solution


@pytest.mark.parametrize("s, output", [("*", 9), ("1*", 18), ("2*", 15)])
class TestSolution:
    def test_numDecodings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numDecodings(
                s,
            )
            == output
        )
