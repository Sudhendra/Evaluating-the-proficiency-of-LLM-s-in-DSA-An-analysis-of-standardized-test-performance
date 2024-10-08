import pytest
from q_0936_stampingTheSequence import Solution


@pytest.mark.parametrize(
    "stamp, target, output", [("abc", "ababc", [0, 2]), ("abca", "aabcaca", [3, 0, 1])]
)
class TestSolution:
    def test_movesToStamp(self, stamp: str, target: str, output: List[int]):
        sc = Solution()
        assert (
            sc.movesToStamp(
                stamp,
                target,
            )
            == output
        )
