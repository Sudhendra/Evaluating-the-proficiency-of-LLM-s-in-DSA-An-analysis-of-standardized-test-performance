import pytest
from q_1023_camelcaseMatching import Solution


@pytest.mark.parametrize(
    "queries, pattern, output",
    [
        (
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
            "FB",
            [True, False, True, True, False],
        ),
        (
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
            "FoBa",
            [True, False, True, False, False],
        ),
        (
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
            "FoBaT",
            [False, True, False, False, False],
        ),
    ],
)
class TestSolution:
    def test_camelMatch(self, queries: List[str], pattern: str, output: List[bool]):
        sc = Solution()
        assert (
            sc.camelMatch(
                queries,
                pattern,
            )
            == output
        )
