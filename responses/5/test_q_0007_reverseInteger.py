import pytest
from q_0007_reverseInteger import Solution


@pytest.mark.parametrize("x, output", [(123, 321), (-123, -321), (120, 21)])
class TestSolution:
    def test_reverse(self, x: int, output: int):
        sc = Solution()
        assert (
            sc.reverse(
                x,
            )
            == output
        )
