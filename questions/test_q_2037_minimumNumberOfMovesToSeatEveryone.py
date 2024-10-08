import pytest
from q_2037_minimumNumberOfMovesToSeatEveryone import Solution


@pytest.mark.parametrize(
    "seats, students, output",
    [
        ([3, 1, 5], [2, 7, 4], 4),
        ([4, 1, 5, 9], [1, 3, 2, 6], 7),
        ([2, 2, 6, 6], [1, 3, 2, 6], 4),
    ],
)
class TestSolution:
    def test_minMovesToSeat(self, seats: List[int], students: List[int], output: int):
        sc = Solution()
        assert (
            sc.minMovesToSeat(
                seats,
                students,
            )
            == output
        )
