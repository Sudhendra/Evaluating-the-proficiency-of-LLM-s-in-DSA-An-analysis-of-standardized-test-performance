import pytest
from q_1478_allocateMailboxes import Solution


@pytest.mark.parametrize(
    "houses, k, output", [([1, 4, 8, 10, 20], 3, 5), ([2, 3, 5, 12, 18], 2, 9)]
)
class TestSolution:
    def test_minDistance(self, houses: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minDistance(
                houses,
                k,
            )
            == output
        )
