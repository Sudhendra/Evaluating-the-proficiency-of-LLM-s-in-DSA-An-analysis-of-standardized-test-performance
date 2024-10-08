import pytest
from q_1017_convertToBase2 import Solution


@pytest.mark.parametrize("n, output", [(2, "110"), (3, "111"), (4, "100")])
class TestSolution:
    def test_baseNeg2(self, n: int, output: str):
        sc = Solution()
        assert (
            sc.baseNeg2(
                n,
            )
            == output
        )
