import pytest
from q_1122_relativeSortArray import Solution


@pytest.mark.parametrize(
    "arr1, arr2, output",
    [
        (
            [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            [2, 1, 4, 3, 9, 6],
            [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        ),
        ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
    ],
)
class TestSolution:
    def test_relativeSortArray(
        self, arr1: List[int], arr2: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.relativeSortArray(
                arr1,
                arr2,
            )
            == output
        )
