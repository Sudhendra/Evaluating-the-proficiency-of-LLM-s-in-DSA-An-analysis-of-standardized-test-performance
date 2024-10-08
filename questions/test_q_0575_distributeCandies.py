import pytest
from q_0575_distributeCandies import Solution


@pytest.mark.parametrize(
    "candyType, output", [([1, 1, 2, 2, 3, 3], 3), ([1, 1, 2, 3], 2), ([6, 6, 6, 6], 1)]
)
class TestSolution:
    def test_distributeCandies(self, candyType: List[int], output: int):
        sc = Solution()
        assert (
            sc.distributeCandies(
                candyType,
            )
            == output
        )
