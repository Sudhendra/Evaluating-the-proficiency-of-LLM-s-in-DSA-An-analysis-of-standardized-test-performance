import pytest
from q_0957_prisonCellsAfterNDays import Solution


@pytest.mark.parametrize(
    "cells, n, output",
    [
        ([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
        ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0]),
    ],
)
class TestSolution:
    def test_prisonAfterNDays(self, cells: List[int], n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.prisonAfterNDays(
                cells,
                n,
            )
            == output
        )
