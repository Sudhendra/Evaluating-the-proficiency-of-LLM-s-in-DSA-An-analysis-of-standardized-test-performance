import pytest
from q_1233_removeSubFoldersFromTheFilesystem import Solution


@pytest.mark.parametrize(
    "folder, output",
    [
        (["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"], ["/a", "/c/d", "/c/f"]),
        (["/a", "/a/b/c", "/a/b/d"], ["/a"]),
        (["/a/b/c", "/a/b/ca", "/a/b/d"], ["/a/b/c", "/a/b/ca", "/a/b/d"]),
    ],
)
class TestSolution:
    def test_removeSubfolders(self, folder: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.removeSubfolders(
                folder,
            )
            == output
        )
