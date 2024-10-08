import pytest
from q_1830_minimumNumberOfOperationsToMakeStringSorted import Solution


@pytest.mark.parametrize("s, output", [("cba", 5), ("aabaa", 2)])
class TestSolution:
    def test_makeStringSorted(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.makeStringSorted(
                s,
            )
            == output
        )
