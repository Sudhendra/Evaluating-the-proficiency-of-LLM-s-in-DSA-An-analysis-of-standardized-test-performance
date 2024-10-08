import pytest
from q_2851_stringTransformation import Solution


@pytest.mark.parametrize(
    "s, t, k, output", [("abcd", "cdab", 2, 2), ("ababab", "ababab", 1, 2)]
)
class TestSolution:
    def test_numberOfWays(self, s: str, t: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfWays(
                s,
                t,
                k,
            )
            == output
        )
