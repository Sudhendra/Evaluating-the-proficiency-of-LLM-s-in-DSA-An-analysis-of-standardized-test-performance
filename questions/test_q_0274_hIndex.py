import pytest
from q_0274_hIndex import Solution


@pytest.mark.parametrize("citations, output", [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1)])
class TestSolution:
    def test_hIndex(self, citations: List[int], output: int):
        sc = Solution()
        assert (
            sc.hIndex(
                citations,
            )
            == output
        )
