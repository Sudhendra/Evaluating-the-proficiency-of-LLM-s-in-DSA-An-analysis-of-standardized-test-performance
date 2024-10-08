import pytest
from q_1860_incrementalMemoryLeak import Solution


@pytest.mark.parametrize(
    "memory1, memory2, output", [(2, 2, [3, 1, 0]), (8, 11, [6, 0, 4])]
)
class TestSolution:
    def test_memLeak(self, memory1: int, memory2: int, output: List[int]):
        sc = Solution()
        assert (
            sc.memLeak(
                memory1,
                memory2,
            )
            == output
        )
