import pytest
from q_0638_shoppingOffers import Solution


@pytest.mark.parametrize(
    "price, special, needs, output",
    [
        ([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2], 14),
        ([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1], 11),
    ],
)
class TestSolution:
    def test_shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.shoppingOffers(
                price,
                special,
                needs,
            )
            == output
        )
