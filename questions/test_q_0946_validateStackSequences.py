import pytest
from q_0946_validateStackSequences import Solution


@pytest.mark.parametrize(
    "pushed, popped, output",
    [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ],
)
class TestSolution:
    def test_validateStackSequences(
        self, pushed: List[int], popped: List[int], output: bool
    ):
        sc = Solution()
        assert (
            sc.validateStackSequences(
                pushed,
                popped,
            )
            == output
        )
