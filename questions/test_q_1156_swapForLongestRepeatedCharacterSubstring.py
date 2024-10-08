import pytest
from q_1156_swapForLongestRepeatedCharacterSubstring import Solution


@pytest.mark.parametrize("text, output", [("ababa", 3), ("aaabaaa", 6), ("aaaaa", 5)])
class TestSolution:
    def test_maxRepOpt1(self, text: str, output: int):
        sc = Solution()
        assert (
            sc.maxRepOpt1(
                text,
            )
            == output
        )
