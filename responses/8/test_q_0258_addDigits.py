import pytest
from q_0258_addDigits import Solution


@pytest.mark.parametrize("num, output", [(38, 2), (0, 0)])
class TestSolution:
    def test_addDigits(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.addDigits(
                num,
            )
            == output
        )
