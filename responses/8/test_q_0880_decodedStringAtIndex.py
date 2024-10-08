import pytest
from q_0880_decodedStringAtIndex import Solution


@pytest.mark.parametrize(
    "s, k, output",
    [("leet2code3", 10, "o"), ("ha22", 5, "h"), ("a2345678999999999999999", 1, "a")],
)
class TestSolution:
    def test_decodeAtIndex(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.decodeAtIndex(
                s,
                k,
            )
            == output
        )
