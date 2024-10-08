import pytest
from q_0808_soupServings import Solution


@pytest.mark.parametrize("n, output", [(50, 0.625), (100, 0.71875)])
class TestSolution:
    def test_soupServings(self, n: int, output: float):
        sc = Solution()
        assert (
            sc.soupServings(
                n,
            )
            == output
        )
