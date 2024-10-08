import pytest
from q_1482_minimumNumberOfDaysToMakeMBouquets import Solution


@pytest.mark.parametrize(
    "bloomDay, m, k, output",
    [
        ([1, 10, 3, 10, 2], 3, 1, 3),
        ([1, 10, 3, 10, 2], 3, 2, -1),
        ([7, 7, 7, 7, 12, 7, 7], 2, 3, 12),
    ],
)
class TestSolution:
    def test_minDays(self, bloomDay: List[int], m: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.minDays(
                bloomDay,
                m,
                k,
            )
            == output
        )
