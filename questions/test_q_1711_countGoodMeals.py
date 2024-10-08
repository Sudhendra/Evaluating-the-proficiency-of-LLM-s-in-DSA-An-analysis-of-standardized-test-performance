import pytest
from q_1711_countGoodMeals import Solution


@pytest.mark.parametrize(
    "deliciousness, output", [([1, 3, 5, 7, 9], 4), ([1, 1, 1, 3, 3, 3, 7], 15)]
)
class TestSolution:
    def test_countPairs(self, deliciousness: List[int], output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                deliciousness,
            )
            == output
        )
