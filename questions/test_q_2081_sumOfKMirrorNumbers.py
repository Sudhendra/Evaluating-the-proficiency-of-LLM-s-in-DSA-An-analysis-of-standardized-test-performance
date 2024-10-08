import pytest
from q_2081_sumOfKMirrorNumbers import Solution


@pytest.mark.parametrize("k, n, output", [(2, 5, 25), (3, 7, 499), (7, 17, 20379000)])
class TestSolution:
    def test_kMirror(self, k: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.kMirror(
                k,
                n,
            )
            == output
        )
