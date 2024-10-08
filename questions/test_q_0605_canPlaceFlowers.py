import pytest
from q_0605_canPlaceFlowers import Solution


@pytest.mark.parametrize(
    "flowerbed, n, output", [([1, 0, 0, 0, 1], 1, True), ([1, 0, 0, 0, 1], 2, False)]
)
class TestSolution:
    def test_canPlaceFlowers(self, flowerbed: List[int], n: int, output: bool):
        sc = Solution()
        assert (
            sc.canPlaceFlowers(
                flowerbed,
                n,
            )
            == output
        )
