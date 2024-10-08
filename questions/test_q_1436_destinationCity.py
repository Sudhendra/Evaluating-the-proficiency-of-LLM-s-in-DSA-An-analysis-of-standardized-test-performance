import pytest
from q_1436_destinationCity import Solution


@pytest.mark.parametrize(
    "paths, output",
    [
        (
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            "Sao Paulo",
        ),
        ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
        ([["A", "Z"]], "Z"),
    ],
)
class TestSolution:
    def test_destCity(self, paths: List[List[str]], output: str):
        sc = Solution()
        assert (
            sc.destCity(
                paths,
            )
            == output
        )
