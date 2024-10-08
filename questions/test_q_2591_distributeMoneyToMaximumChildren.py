import pytest
from q_2591_distributeMoneyToMaximumChildren import Solution


@pytest.mark.parametrize("money, children, output", [(20, 3, 1), (16, 2, 2)])
class TestSolution:
    def test_distMoney(self, money: int, children: int, output: int):
        sc = Solution()
        assert (
            sc.distMoney(
                money,
                children,
            )
            == output
        )
