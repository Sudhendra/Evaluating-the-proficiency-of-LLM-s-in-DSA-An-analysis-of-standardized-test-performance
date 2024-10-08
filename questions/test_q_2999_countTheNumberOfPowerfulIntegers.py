import pytest
from q_2999_countTheNumberOfPowerfulIntegers import Solution


@pytest.mark.parametrize(
    "start, finish, limit, s, output",
    [(1, 6000, 4, "124", 5), (15, 215, 6, "10", 2), (1000, 2000, 4, "3000", 0)],
)
class TestSolution:
    def test_numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str, output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfPowerfulInt(
                start,
                finish,
                limit,
                s,
            )
            == output
        )
