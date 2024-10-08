import pytest
from q_0844_backspaceStringCompare import Solution


@pytest.mark.parametrize(
    "s, t, output",
    [("ab#c", "ad#c", True), ("ab##", "c#d#", True), ("a#c", "b", False)],
)
class TestSolution:
    def test_backspaceCompare(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.backspaceCompare(
                s,
                t,
            )
            == output
        )
