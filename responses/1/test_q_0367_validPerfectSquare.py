import pytest
from q_0367_validPerfectSquare import Solution


@pytest.mark.parametrize("num, output", [(16, True), (14, False)])
class TestSolution:
    def test_isPerfectSquare(self, num: int, output: bool):
        sc = Solution()
        assert (
            sc.isPerfectSquare(
                num,
            )
            == output
        )
