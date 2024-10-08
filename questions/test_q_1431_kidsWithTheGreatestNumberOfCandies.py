import pytest
from q_1431_kidsWithTheGreatestNumberOfCandies import Solution


@pytest.mark.parametrize(
    "candies, extraCandies, output",
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
    ],
)
class TestSolution:
    def test_kidsWithCandies(
        self, candies: List[int], extraCandies: int, output: List[bool]
    ):
        sc = Solution()
        assert (
            sc.kidsWithCandies(
                candies,
                extraCandies,
            )
            == output
        )
