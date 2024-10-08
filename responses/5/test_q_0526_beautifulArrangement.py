import pytest
from q_0526_beautifulArrangement import Solution


@pytest.mark.parametrize("n, output", [(2, 2), (1, 1)])
class TestSolution:
    def test_countArrangement(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countArrangement(
                n,
            )
            == output
        )
