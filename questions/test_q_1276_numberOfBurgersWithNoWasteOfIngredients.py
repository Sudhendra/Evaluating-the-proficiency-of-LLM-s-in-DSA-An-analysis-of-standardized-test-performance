import pytest
from q_1276_numberOfBurgersWithNoWasteOfIngredients import Solution


@pytest.mark.parametrize(
    "tomatoSlices, cheeseSlices, output", [(16, 7, [1, 6]), (17, 4, []), (4, 17, [])]
)
class TestSolution:
    def test_numOfBurgers(
        self, tomatoSlices: int, cheeseSlices: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.numOfBurgers(
                tomatoSlices,
                cheeseSlices,
            )
            == output
        )
