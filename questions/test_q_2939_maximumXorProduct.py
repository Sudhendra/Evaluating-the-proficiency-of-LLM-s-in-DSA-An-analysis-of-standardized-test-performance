import pytest
from q_2939_maximumXorProduct import Solution


@pytest.mark.parametrize(
    "a, b, n, output", [(12, 5, 4, 98), (6, 7, 5, 930), (1, 6, 3, 12)]
)
class TestSolution:
    def test_maximumXorProduct(self, a: int, b: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.maximumXorProduct(
                a,
                b,
                n,
            )
            == output
        )
