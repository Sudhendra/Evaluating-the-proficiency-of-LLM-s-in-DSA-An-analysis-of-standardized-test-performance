import pytest
from q_1948_deleteDuplicateFoldersInSystem import Solution


@pytest.mark.parametrize(
    "paths, output",
    [
        (
            [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]],
            [["d"], ["d", "a"]],
        ),
        (
            [
                ["a"],
                ["c"],
                ["a", "b"],
                ["c", "b"],
                ["a", "b", "x"],
                ["a", "b", "x", "y"],
                ["w"],
                ["w", "y"],
            ],
            [["c"], ["c", "b"], ["a"], ["a", "b"]],
        ),
        (
            [["a", "b"], ["c", "d"], ["c"], ["a"]],
            [["c"], ["c", "d"], ["a"], ["a", "b"]],
        ),
    ],
)
class TestSolution:
    def test_deleteDuplicateFolder(
        self, paths: List[List[str]], output: List[List[str]]
    ):
        sc = Solution()
        assert (
            sc.deleteDuplicateFolder(
                paths,
            )
            == output
        )
