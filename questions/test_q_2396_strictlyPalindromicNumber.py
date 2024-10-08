import pytest
from q_2396_strictlyPalindromicNumber import Solution


@pytest.mark.parametrize("n, output", [(9, False), (4, False)])
class TestSolution:
    def test_isStrictlyPalindromic(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isStrictlyPalindromic(
                n,
            )
            == output
        )
