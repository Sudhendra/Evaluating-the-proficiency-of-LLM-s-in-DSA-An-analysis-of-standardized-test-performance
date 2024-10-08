import pytest
from q_0752_openTheLock import Solution


@pytest.mark.parametrize(
    "deadends, target, output",
    [
        (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1),
    ],
)
class TestSolution:
    def test_openLock(self, deadends: List[str], target: str, output: int):
        sc = Solution()
        assert (
            sc.openLock(
                deadends,
                target,
            )
            == output
        )
