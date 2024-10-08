import pytest
from q_1138_alphabetBoardPath import Solution


@pytest.mark.parametrize(
    "target, output", [("leet", "DDR!UURRR!!DDD!"), ("code", "RR!DDRR!UUL!R!")]
)
class TestSolution:
    def test_alphabetBoardPath(self, target: str, output: str):
        sc = Solution()
        assert (
            sc.alphabetBoardPath(
                target,
            )
            == output
        )
