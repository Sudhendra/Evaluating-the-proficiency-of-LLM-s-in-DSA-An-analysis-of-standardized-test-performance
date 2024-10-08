import pytest
from q_2092_findAllPeopleWithSecret import Solution


@pytest.mark.parametrize(
    "n, meetings, firstPerson, output",
    [
        (6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1, [0, 1, 2, 3, 5]),
        (4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3, [0, 1, 3]),
        (5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1, [0, 1, 2, 3, 4]),
    ],
)
class TestSolution:
    def test_findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findAllPeople(
                n,
                meetings,
                firstPerson,
            )
            == output
        )
