import pytest
from q_0476_numberComplement import Solution


@pytest.mark.parametrize("num, output", [(5, 2), (1, 0)])
class TestSolution:
    def test_findComplement(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.findComplement(
                num,
            )
            == output
        )
