import pytest
from q_0338_countingBits import Solution


@pytest.mark.parametrize("n, output", [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2])])
class TestSolution:
    def test_countBits(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.countBits(
                n,
            )
            == output
        )
