import pytest
from q_1452_peopleWhoseListOfFavoriteCompaniesIsNotASubsetOfAnotherList import Solution


@pytest.mark.parametrize(
    "favoriteCompanies, output",
    [
        (
            [
                ["leetcode", "google", "facebook"],
                ["google", "microsoft"],
                ["google", "facebook"],
                ["google"],
                ["amazon"],
            ],
            [0, 1, 4],
        ),
        (
            [
                ["leetcode", "google", "facebook"],
                ["leetcode", "amazon"],
                ["facebook", "google"],
            ],
            [0, 1],
        ),
        ([["leetcode"], ["google"], ["facebook"], ["amazon"]], [0, 1, 2, 3]),
    ],
)
class TestSolution:
    def test_peopleIndexes(self, favoriteCompanies: List[List[str]], output: List[int]):
        sc = Solution()
        assert (
            sc.peopleIndexes(
                favoriteCompanies,
            )
            == output
        )
