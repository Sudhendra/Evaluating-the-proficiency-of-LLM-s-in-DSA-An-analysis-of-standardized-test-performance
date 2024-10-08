import pytest
from q_2391_minimumAmountOfTimeToCollectGarbage import Solution


@pytest.mark.parametrize(
    "garbage, travel, output",
    [(["G", "P", "GP", "GG"], [2, 4, 3], 21), (["MMM", "PGM", "GP"], [3, 10], 37)],
)
class TestSolution:
    def test_garbageCollection(
        self, garbage: List[str], travel: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.garbageCollection(
                garbage,
                travel,
            )
            == output
        )
