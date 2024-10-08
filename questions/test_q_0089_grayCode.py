import pytest
from q_0089_grayCode import Solution


@pytest.mark.parametrize("n, output", [(2, [0, 1, 3, 2]), (1, [0, 1])])
class TestSolution:
    def test_grayCode(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.grayCode(
                n,
            )
            == output
        )
