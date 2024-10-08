import pytest
from q_1036_escapeALargeMaze import Solution


@pytest.mark.parametrize(
    "blocked, source, target, output",
    [([[0, 1], [1, 0]], [0, 0], [0, 2], False), ([], [0, 0], [999999, 999999], True)],
)
class TestSolution:
    def test_isEscapePossible(
        self,
        blocked: List[List[int]],
        source: List[int],
        target: List[int],
        output: bool,
    ):
        sc = Solution()
        assert (
            sc.isEscapePossible(
                blocked,
                source,
                target,
            )
            == output
        )
