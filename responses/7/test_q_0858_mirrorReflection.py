import pytest
from q_0858_mirrorReflection import Solution


@pytest.mark.parametrize("p, q, output", [(2, 1, 2), (3, 1, 1)])
class TestSolution:
    def test_mirrorReflection(self, p: int, q: int, output: int):
        sc = Solution()
        assert (
            sc.mirrorReflection(
                p,
                q,
            )
            == output
        )
