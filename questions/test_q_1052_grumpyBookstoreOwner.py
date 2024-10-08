import pytest
from q_1052_grumpyBookstoreOwner import Solution


@pytest.mark.parametrize(
    "customers, grumpy, minutes, output",
    [([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16), ([1], [0], 1, 1)],
)
class TestSolution:
    def test_maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxSatisfied(
                customers,
                grumpy,
                minutes,
            )
            == output
        )
