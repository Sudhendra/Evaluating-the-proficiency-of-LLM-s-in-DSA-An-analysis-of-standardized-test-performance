import pytest
from q_2165_smallestValueOfTheRearrangedNumber import Solution


@pytest.mark.parametrize("num, output", [(310, 103), (-7605, -7650)])
class TestSolution:
    def test_smallestNumber(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.smallestNumber(
                num,
            )
            == output
        )
