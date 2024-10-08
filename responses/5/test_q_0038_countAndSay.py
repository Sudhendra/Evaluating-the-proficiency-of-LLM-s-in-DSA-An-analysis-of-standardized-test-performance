import pytest
from q_0038_countAndSay import Solution


@pytest.mark.parametrize("n, output", [(1, "1"), (4, "1211")])
class TestSolution:
    def test_countAndSay(self, n: int, output: str):
        sc = Solution()
        assert (
            sc.countAndSay(
                n,
            )
            == output
        )
