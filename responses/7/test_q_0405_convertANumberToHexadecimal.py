import pytest
from q_0405_convertANumberToHexadecimal import Solution


@pytest.mark.parametrize("num, output", [(26, "1a"), (-1, "ffffffff")])
class TestSolution:
    def test_toHex(self, num: int, output: str):
        sc = Solution()
        assert (
            sc.toHex(
                num,
            )
            == output
        )
