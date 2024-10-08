import pytest
from q_0599_minimumIndexSumOfTwoLists import Solution


@pytest.mark.parametrize(
    "list1, list2, output",
    [
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            [
                "Piatti",
                "The Grill at Torrey Pines",
                "Hungry Hunter Steakhouse",
                "Shogun",
            ],
            ["Shogun"],
        ),
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"],
            ["Shogun"],
        ),
        (["happy", "sad", "good"], ["sad", "happy", "good"], ["sad", "happy"]),
    ],
)
class TestSolution:
    def test_findRestaurant(
        self, list1: List[str], list2: List[str], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.findRestaurant(
                list1,
                list2,
            )
            == output
        )
