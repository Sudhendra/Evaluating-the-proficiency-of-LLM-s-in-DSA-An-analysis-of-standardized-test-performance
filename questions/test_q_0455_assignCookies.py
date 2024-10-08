import pytest
from q_0455_assignCookies import Solution


@pytest.mark.parametrize(
    "g, s, output", [([1, 2, 3], [1, 1], 1), ([1, 2], [1, 2, 3], 2)]
)
class TestSolution:
    def test_findContentChildren(self, g: List[int], s: List[int], output: int):
        sc = Solution()
        assert (
            sc.findContentChildren(
                g,
                s,
            )
            == output
        )
