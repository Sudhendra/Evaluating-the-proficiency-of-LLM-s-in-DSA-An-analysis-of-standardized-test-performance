import pytest
from q_0483_smallestGoodBase import Solution


@pytest.mark.parametrize(
    "n, output",
    [("13", "3"), ("4681", "8"), ("1000000000000000000", "999999999999999999")],
)
class TestSolution:
    def test_smallestGoodBase(self, n: str, output: str):
        sc = Solution()
        assert (
            sc.smallestGoodBase(
                n,
            )
            == output
        )
