import pytest
from q_2729_checkIfTheNumberIsFascinating import Solution


@pytest.mark.parametrize("n, output", [(192, True), (100, False)])
class TestSolution:
    def test_isFascinating(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isFascinating(
                n,
            )
            == output
        )
