import pytest
from q_0664_strangePrinter import Solution


@pytest.mark.parametrize("s, output", [("aaabbb", 2), ("aba", 2)])
class TestSolution:
    def test_strangePrinter(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.strangePrinter(
                s,
            )
            == output
        )
