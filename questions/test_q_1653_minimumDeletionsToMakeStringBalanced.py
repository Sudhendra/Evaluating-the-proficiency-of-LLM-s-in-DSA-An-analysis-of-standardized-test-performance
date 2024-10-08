import pytest
from q_1653_minimumDeletionsToMakeStringBalanced import Solution


@pytest.mark.parametrize("s, output", [("aababbab", 2), ("bbaaaaabb", 2)])
class TestSolution:
    def test_minimumDeletions(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumDeletions(
                s,
            )
            == output
        )
