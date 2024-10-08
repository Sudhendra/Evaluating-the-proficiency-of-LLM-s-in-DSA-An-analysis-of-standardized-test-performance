import pytest
from q_0474_onesAndZeroes import Solution


@pytest.mark.parametrize(
    "strs, m, n, output",
    [(["10", "0001", "111001", "1", "0"], 5, 3, 4), (["10", "0", "1"], 1, 1, 2)],
)
class TestSolution:
    def test_findMaxForm(self, strs: List[str], m: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.findMaxForm(
                strs,
                m,
                n,
            )
            == output
        )
