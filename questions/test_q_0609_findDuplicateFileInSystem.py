import pytest
from q_0609_findDuplicateFileInSystem import Solution


@pytest.mark.parametrize(
    "paths, output",
    [
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            [
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        ),
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]],
        ),
    ],
)
class TestSolution:
    def test_findDuplicate(self, paths: List[str], output: List[List[str]]):
        sc = Solution()
        assert (
            sc.findDuplicate(
                paths,
            )
            == output
        )
