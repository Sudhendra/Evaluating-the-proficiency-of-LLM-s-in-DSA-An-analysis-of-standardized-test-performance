import pytest
from q_0816_ambiguousCoordinates import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("(123)", ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]),
        (
            "(0123)",
            [
                "(0, 1.23)",
                "(0, 12.3)",
                "(0, 123)",
                "(0.1, 2.3)",
                "(0.1, 23)",
                "(0.12, 3)",
            ],
        ),
        ("(00011)", ["(0, 0.011)", "(0.001, 1)"]),
    ],
)
class TestSolution:
    def test_ambiguousCoordinates(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.ambiguousCoordinates(
                s,
            )
            == output
        )
