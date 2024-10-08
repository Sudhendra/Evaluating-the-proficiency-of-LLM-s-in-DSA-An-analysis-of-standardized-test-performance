import pytest
from q_1388_pizzaWith3NSlices import Solution


@pytest.mark.parametrize(
    "slices, output", [([1, 2, 3, 4, 5, 6], 10), ([8, 9, 8, 6, 1, 1], 16)]
)
class TestSolution:
    def test_maxSizeSlices(self, slices: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSizeSlices(
                slices,
            )
            == output
        )
