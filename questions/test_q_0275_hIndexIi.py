import pytest
from q_0275_hIndexIi import Solution


@pytest.mark.parametrize("citations, output", [([0, 1, 3, 5, 6], 3), ([1, 2, 100], 2)])
class TestSolution:
    def test_hIndex(self, citations: List[int], output: int):
        sc = Solution()
        assert (
            sc.hIndex(
                citations,
            )
            == output
        )
