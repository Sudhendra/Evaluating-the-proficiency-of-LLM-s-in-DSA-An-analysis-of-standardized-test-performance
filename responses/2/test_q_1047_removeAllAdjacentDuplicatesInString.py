import pytest
from q_1047_removeAllAdjacentDuplicatesInString import Solution


@pytest.mark.parametrize("s, output", [("abbaca", "ca"), ("azxxzy", "ay")])
class TestSolution:
    def test_removeDuplicates(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.removeDuplicates(
                s,
            )
            == output
        )
