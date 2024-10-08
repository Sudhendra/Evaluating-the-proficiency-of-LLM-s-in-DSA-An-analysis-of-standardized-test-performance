import pytest
from q_2167_minimumTimeToRemoveAllCarsContainingIllegalGoods import Solution


@pytest.mark.parametrize("s, output", [("**11**00**1**0**1**", 5), ("00**1**0", 2)])
class TestSolution:
    def test_minimumTime(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumTime(
                s,
            )
            == output
        )
