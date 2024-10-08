import pytest
from q_2115_findAllPossibleRecipesFromGivenSupplies import Solution


@pytest.mark.parametrize(
    "recipes, ingredients, supplies, output",
    [
        (["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"], ["bread"]),
        (
            ["bread", "sandwich"],
            [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich"],
        ),
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich", "burger"],
        ),
    ],
)
class TestSolution:
    def test_findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
        output: List[str],
    ):
        sc = Solution()
        assert (
            sc.findAllRecipes(
                recipes,
                ingredients,
                supplies,
            )
            == output
        )
