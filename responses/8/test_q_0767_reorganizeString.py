import pytest
from q_0767_reorganizeString import Solution


@pytest.mark.parametrize("s, output", [("aab", "aba"), ("aaab", "")])
class TestSolution:
    def test_reorganizeString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reorganizeString(
                s,
            )
            == output
        )
