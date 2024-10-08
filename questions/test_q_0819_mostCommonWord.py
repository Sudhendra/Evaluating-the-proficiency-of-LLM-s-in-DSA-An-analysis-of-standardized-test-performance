import pytest
from q_0819_mostCommonWord import Solution


@pytest.mark.parametrize(
    "paragraph, banned, output",
    [
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
        ("a.", [], "a"),
    ],
)
class TestSolution:
    def test_mostCommonWord(self, paragraph: str, banned: List[str], output: str):
        sc = Solution()
        assert (
            sc.mostCommonWord(
                paragraph,
                banned,
            )
            == output
        )
