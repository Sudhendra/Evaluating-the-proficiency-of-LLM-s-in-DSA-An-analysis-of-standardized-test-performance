import pytest
from q_0848_shiftingLetters import Solution


@pytest.mark.parametrize(
    "s, shifts, output", [("abc", [3, 5, 9], "rpl"), ("aaa", [1, 2, 3], "gfd")]
)
class TestSolution:
    def test_shiftingLetters(self, s: str, shifts: List[int], output: str):
        sc = Solution()
        assert (
            sc.shiftingLetters(
                s,
                shifts,
            )
            == output
        )
