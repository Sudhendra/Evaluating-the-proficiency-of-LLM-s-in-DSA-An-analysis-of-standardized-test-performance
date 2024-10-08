import pytest
from q_1054_distantBarcodes import Solution


@pytest.mark.parametrize(
    "barcodes, output",
    [
        ([1, 1, 1, 2, 2, 2], [2, 1, 2, 1, 2, 1]),
        ([1, 1, 1, 1, 2, 2, 3, 3], [1, 3, 1, 3, 1, 2, 1, 2]),
    ],
)
class TestSolution:
    def test_rearrangeBarcodes(self, barcodes: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.rearrangeBarcodes(
                barcodes,
            )
            == output
        )
