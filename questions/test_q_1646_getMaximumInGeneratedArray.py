import pytest
from q_1646_getMaximumInGeneratedArray import Solution


@pytest.mark.parametrize("n, output", [(7, 3), (2, 1), (3, 2)])
class TestSolution:
    def test_getMaximumGenerated(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.getMaximumGenerated(
                n,
            )
            == output
        )
