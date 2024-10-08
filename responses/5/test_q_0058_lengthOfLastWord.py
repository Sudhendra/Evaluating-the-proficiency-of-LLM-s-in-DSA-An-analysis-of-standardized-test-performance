import pytest
from q_0058_lengthOfLastWord import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
class TestSolution:
    def test_lengthOfLastWord(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.lengthOfLastWord(
                s,
            )
            == output
        )
