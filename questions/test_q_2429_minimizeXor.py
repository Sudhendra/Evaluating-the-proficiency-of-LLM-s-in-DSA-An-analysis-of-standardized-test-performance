import pytest
from q_2429_minimizeXor import Solution


@pytest.mark.parametrize("num1, num2, output", [(3, 5, 3), (1, 12, 3)])
class TestSolution:
    def test_minimizeXor(self, num1: int, num2: int, output: int):
        sc = Solution()
        assert (
            sc.minimizeXor(
                num1,
                num2,
            )
            == output
        )
