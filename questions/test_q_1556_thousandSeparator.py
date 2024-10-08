import pytest
from q_1556_thousandSeparator import Solution


@pytest.mark.parametrize("n, output", [(987, "987"), (1234, "1.234")])
class TestSolution:
    def test_thousandSeparator(self, n: int, output: str):
        sc = Solution()
        assert (
            sc.thousandSeparator(
                n,
            )
            == output
        )
