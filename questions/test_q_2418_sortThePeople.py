import pytest
from q_2418_sortThePeople import Solution


@pytest.mark.parametrize(
    "names, heights, output",
    [
        (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
        (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
    ],
)
class TestSolution:
    def test_sortPeople(self, names: List[str], heights: List[int], output: List[str]):
        sc = Solution()
        assert (
            sc.sortPeople(
                names,
                heights,
            )
            == output
        )
