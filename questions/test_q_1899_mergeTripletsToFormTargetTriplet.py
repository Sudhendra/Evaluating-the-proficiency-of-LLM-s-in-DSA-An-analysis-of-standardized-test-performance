import pytest
from q_1899_mergeTripletsToFormTargetTriplet import Solution


@pytest.mark.parametrize(
    "triplets, target, output",
    [
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
    ],
)
class TestSolution:
    def test_mergeTriplets(
        self, triplets: List[List[int]], target: List[int], output: bool
    ):
        sc = Solution()
        assert (
            sc.mergeTriplets(
                triplets,
                target,
            )
            == output
        )
