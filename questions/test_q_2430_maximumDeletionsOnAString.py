import pytest
from q_2430_maximumDeletionsOnAString import Solution


@pytest.mark.parametrize("s, output", [("abcabcdabc", 2), ("aaabaab", 4), ("aaaaa", 5)])
class TestSolution:
    def test_deleteString(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.deleteString(
                s,
            )
            == output
        )
