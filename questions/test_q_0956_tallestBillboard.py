import pytest
from q_0956_tallestBillboard import Solution


@pytest.mark.parametrize(
    "rods, output", [([1, 2, 3, 6], 6), ([1, 2, 3, 4, 5, 6], 10), ([1, 2], 0)]
)
class TestSolution:
    def test_tallestBillboard(self, rods: List[int], output: int):
        sc = Solution()
        assert (
            sc.tallestBillboard(
                rods,
            )
            == output
        )
