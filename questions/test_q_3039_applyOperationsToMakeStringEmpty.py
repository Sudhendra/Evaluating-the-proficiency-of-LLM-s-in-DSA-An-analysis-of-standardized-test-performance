import pytest
from q_3039_applyOperationsToMakeStringEmpty import Solution


@pytest.mark.parametrize("s, output", [("aabcbbca", "ba"), ("abcd", "abcd")])
class TestSolution:
    def test_lastNonEmptyString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.lastNonEmptyString(
                s,
            )
            == output
        )
