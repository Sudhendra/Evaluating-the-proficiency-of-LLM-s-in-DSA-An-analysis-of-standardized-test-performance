import pytest
from q_1103_distributeCandiesToPeople import Solution


@pytest.mark.parametrize(
    "candies, num_people, output", [(7, 4, [1, 2, 3, 1]), (10, 3, [5, 2, 3])]
)
class TestSolution:
    def test_distributeCandies(self, candies: int, num_people: int, output: List[int]):
        sc = Solution()
        assert (
            sc.distributeCandies(
                candies,
                num_people,
            )
            == output
        )
