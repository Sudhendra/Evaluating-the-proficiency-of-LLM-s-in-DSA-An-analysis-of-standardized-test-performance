import pytest
from q_0679_24Game import Solution


@pytest.mark.parametrize("cards, output", [([4, 1, 8, 7], True), ([1, 2, 1, 2], False)])
class TestSolution:
    def test_judgePoint24(self, cards: List[int], output: bool):
        sc = Solution()
        assert (
            sc.judgePoint24(
                cards,
            )
            == output
        )
