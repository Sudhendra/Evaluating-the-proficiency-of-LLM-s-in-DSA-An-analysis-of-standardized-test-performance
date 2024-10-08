import pytest
from q_0753_crackingTheSafe import Solution


@pytest.mark.parametrize("n, k, output", [(1, 2, "10"), (2, 2, "01100")])
class TestSolution:
    def test_crackSafe(self, n: int, k: int, output: str):
        sc = Solution()
        assert (
            sc.crackSafe(
                n,
                k,
            )
            == output
        )
