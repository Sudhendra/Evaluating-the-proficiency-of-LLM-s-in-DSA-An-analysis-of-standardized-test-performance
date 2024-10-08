import pytest
from q_1733_minimumNumberOfPeopleToTeach import Solution


@pytest.mark.parametrize(
    "n, languages, friendships, output",
    [
        (2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]], 1),
        (3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]], 2),
    ],
)
class TestSolution:
    def test_minimumTeachings(
        self,
        n: int,
        languages: List[List[int]],
        friendships: List[List[int]],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumTeachings(
                n,
                languages,
                friendships,
            )
            == output
        )
