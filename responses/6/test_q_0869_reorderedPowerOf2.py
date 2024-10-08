import pytest
from q_0869_reorderedPowerOf2 import Solution


@pytest.mark.parametrize("n, output", [(1, True), (10, False)])
class TestSolution:
    def test_reorderedPowerOf2(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.reorderedPowerOf2(
                n,
            )
            == output
        )
