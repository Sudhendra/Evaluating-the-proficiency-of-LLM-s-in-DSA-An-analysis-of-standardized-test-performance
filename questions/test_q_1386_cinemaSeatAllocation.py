import pytest
from q_1386_cinemaSeatAllocation import Solution


@pytest.mark.parametrize(
    "n, reservedSeats, output",
    [
        (3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 4),
        (2, [[2, 1], [1, 8], [2, 6]], 2),
        (4, [[4, 3], [1, 4], [4, 6], [1, 7]], 4),
    ],
)
class TestSolution:
    def test_maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.maxNumberOfFamilies(
                n,
                reservedSeats,
            )
            == output
        )
