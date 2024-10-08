import pytest
from q_0860_lemonadeChange import Solution


@pytest.mark.parametrize(
    "bills, output", [([5, 5, 5, 10, 20], True), ([5, 5, 10, 10, 20], False)]
)
class TestSolution:
    def test_lemonadeChange(self, bills: List[int], output: bool):
        sc = Solution()
        assert (
            sc.lemonadeChange(
                bills,
            )
            == output
        )
