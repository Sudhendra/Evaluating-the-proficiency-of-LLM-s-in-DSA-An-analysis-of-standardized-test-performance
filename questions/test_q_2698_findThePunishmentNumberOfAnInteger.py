import pytest
from q_2698_findThePunishmentNumberOfAnInteger import Solution


@pytest.mark.parametrize("n, output", [(10, 182), (37, 1478)])
class TestSolution:
    def test_punishmentNumber(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.punishmentNumber(
                n,
            )
            == output
        )
