import pytest
from q_0344_reverseString import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
class TestSolution:
    def test_reverseString(self, s: List[str], output: None):
        sc = Solution()
        assert (
            sc.reverseString(
                s,
            )
            == output
        )
