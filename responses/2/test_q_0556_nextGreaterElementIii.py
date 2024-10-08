import pytest
from q_0556_nextGreaterElementIii import Solution


@pytest.mark.parametrize("n, output", [(12, 21), (21, -1)])
class TestSolution:
    def test_nextGreaterElement(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.nextGreaterElement(
                n,
            )
            == output
        )
