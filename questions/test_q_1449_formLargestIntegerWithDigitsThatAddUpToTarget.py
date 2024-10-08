import pytest
from q_1449_formLargestIntegerWithDigitsThatAddUpToTarget import Solution


@pytest.mark.parametrize(
    "cost, target, output",
    [
        ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9, "7772"),
        ([7, 6, 5, 5, 5, 6, 8, 7, 8], 12, "85"),
        ([2, 4, 6, 2, 4, 6, 4, 4, 4], 5, "0"),
    ],
)
class TestSolution:
    def test_largestNumber(self, cost: List[int], target: int, output: str):
        sc = Solution()
        assert (
            sc.largestNumber(
                cost,
                target,
            )
            == output
        )
