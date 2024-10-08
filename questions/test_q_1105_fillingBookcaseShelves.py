import pytest
from q_1105_fillingBookcaseShelves import Solution


@pytest.mark.parametrize(
    "books, shelfWidth, output",
    [
        ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4, 6),
        ([[1, 3], [2, 4], [3, 2]], 6, 4),
    ],
)
class TestSolution:
    def test_minHeightShelves(
        self, books: List[List[int]], shelfWidth: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minHeightShelves(
                books,
                shelfWidth,
            )
            == output
        )
