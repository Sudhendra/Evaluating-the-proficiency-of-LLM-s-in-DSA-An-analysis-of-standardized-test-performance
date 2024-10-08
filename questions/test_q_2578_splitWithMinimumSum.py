import pytest
from q_2578_splitWithMinimumSum import Solution


@pytest.mark.parametrize("num, output", [(4325, 59), (687, 75)])
class TestSolution:
    def test_splitNum(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.splitNum(
                num,
            )
            == output
        )
