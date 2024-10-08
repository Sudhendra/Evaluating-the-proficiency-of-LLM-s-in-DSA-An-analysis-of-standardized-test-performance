import pytest
from q_1898_maximumNumberOfRemovableCharacters import Solution


@pytest.mark.parametrize(
    "s, p, removable, output",
    [
        ("abcacb", "ab", [3, 1, 0], 2),
        ("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6], 1),
        ("abcab", "abc", [0, 1, 2, 3, 4], 0),
    ],
)
class TestSolution:
    def test_maximumRemovals(self, s: str, p: str, removable: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumRemovals(
                s,
                p,
                removable,
            )
            == output
        )
