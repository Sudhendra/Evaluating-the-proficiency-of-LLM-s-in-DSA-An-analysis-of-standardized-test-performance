import pytest
from q_1356_sortIntegersByTheNumberOf1Bits import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
        (
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ],
)
class TestSolution:
    def test_sortByBits(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortByBits(
                arr,
            )
            == output
        )
