import pytest
from q_0201_bitwiseAndOfNumbersRange import Solution


@pytest.mark.parametrize(
    "left, right, output", [(5, 7, 4), (0, 0, 0), (1, 2147483647, 0)]
)
class TestSolution:
    def test_rangeBitwiseAnd(self, left: int, right: int, output: int):
        sc = Solution()
        assert (
            sc.rangeBitwiseAnd(
                left,
                right,
            )
            == output
        )
