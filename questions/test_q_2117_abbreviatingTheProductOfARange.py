import pytest
from q_2117_abbreviatingTheProductOfARange import Solution


@pytest.mark.parametrize(
    "left, right, output",
    [(1, 4, "24e0"), (2, 11, "399168e2"), (371, 375, "7219856259e3")],
)
class TestSolution:
    def test_abbreviateProduct(self, left: int, right: int, output: str):
        sc = Solution()
        assert (
            sc.abbreviateProduct(
                left,
                right,
            )
            == output
        )
