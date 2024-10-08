import pytest
from q_2582_passThePillow import Solution


@pytest.mark.parametrize("n, time, output", [(4, 5, 2), (3, 2, 3)])
class TestSolution:
    def test_passThePillow(self, n: int, time: int, output: int):
        sc = Solution()
        assert (
            sc.passThePillow(
                n,
                time,
            )
            == output
        )
