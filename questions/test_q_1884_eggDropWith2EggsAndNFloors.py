import pytest
from q_1884_eggDropWith2EggsAndNFloors import Solution


@pytest.mark.parametrize("n, output", [(2, 2), (100, 14)])
class TestSolution:
    def test_twoEggDrop(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.twoEggDrop(
                n,
            )
            == output
        )
