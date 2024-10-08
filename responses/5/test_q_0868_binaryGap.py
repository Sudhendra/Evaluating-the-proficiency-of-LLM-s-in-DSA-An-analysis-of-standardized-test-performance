import pytest
from q_0868_binaryGap import Solution


@pytest.mark.parametrize("n, output", [(22, 2), (8, 0), (5, 2)])
class TestSolution:
    def test_binaryGap(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.binaryGap(
                n,
            )
            == output
        )
