import pytest
from q_2517_maximumTastinessOfCandyBasket import Solution


@pytest.mark.parametrize(
    "price, k, output",
    [([13, 5, 1, 8, 21, 2], 3, 8), ([1, 3, 1], 2, 2), ([7, 7, 7, 7], 2, 0)],
)
class TestSolution:
    def test_maximumTastiness(self, price: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumTastiness(
                price,
                k,
            )
            == output
        )
