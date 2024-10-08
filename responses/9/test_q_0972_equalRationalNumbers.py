import pytest
from q_0972_equalRationalNumbers import Solution


@pytest.mark.parametrize(
    "s, t, output",
    [
        ("0.(52)", "0.5(25)", True),
        ("0.1666(6)", "0.166(66)", True),
        ("0.9(9)", "1.", True),
    ],
)
class TestSolution:
    def test_isRationalEqual(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.isRationalEqual(
                s,
                t,
            )
            == output
        )
