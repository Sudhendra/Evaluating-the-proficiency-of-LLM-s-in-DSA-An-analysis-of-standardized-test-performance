import pytest
from q_1446_consecutiveCharacters import Solution


@pytest.mark.parametrize("s, output", [("leetcode", 2), ("abbcccddddeeeeedcba", 5)])
class TestSolution:
    def test_maxPower(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxPower(
                s,
            )
            == output
        )
