import pytest
from q_3076_shortestUncommonSubstringInAnArray import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        (["cab", "ad", "bad", "c"], ["ab", "", "ba", ""]),
        (["abc", "bcd", "abcd"], ["", "", "abcd"]),
    ],
)
class TestSolution:
    def test_shortestSubstrings(self, arr: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.shortestSubstrings(
                arr,
            )
            == output
        )
