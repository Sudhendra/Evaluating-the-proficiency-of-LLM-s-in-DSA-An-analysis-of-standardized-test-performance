import pytest
from q_0937_reorderDataInLogFiles import Solution


@pytest.mark.parametrize(
    "logs, output",
    [
        (
            [
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero",
            ],
            [
                "let1 art can",
                "let3 art zero",
                "let2 own kit dig",
                "dig1 8 1 5 1",
                "dig2 3 6",
            ],
        ),
        (
            ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
            ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
        ),
    ],
)
class TestSolution:
    def test_reorderLogFiles(self, logs: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.reorderLogFiles(
                logs,
            )
            == output
        )
