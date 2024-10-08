import pytest
from q_0332_reconstructItinerary import Solution


@pytest.mark.parametrize(
    "tickets, output",
    [
        (
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ),
        (
            [
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
    ],
)
class TestSolution:
    def test_findItinerary(self, tickets: List[List[str]], output: List[str]):
        sc = Solution()
        assert (
            sc.findItinerary(
                tickets,
            )
            == output
        )
