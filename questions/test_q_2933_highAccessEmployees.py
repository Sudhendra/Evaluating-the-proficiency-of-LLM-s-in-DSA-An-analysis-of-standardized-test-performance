import pytest
from q_2933_highAccessEmployees import Solution


@pytest.mark.parametrize(
    "access_times, output",
    [
        (
            [["a", "0549"], ["b", "0457"], ["a", "0532"], ["a", "0621"], ["b", "0540"]],
            ["a"],
        ),
        (
            [
                ["d", "0002"],
                ["c", "0808"],
                ["c", "0829"],
                ["e", "0215"],
                ["d", "1508"],
                ["d", "1444"],
                ["d", "1410"],
                ["c", "0809"],
            ],
            ["c", "d"],
        ),
        (
            [
                ["cd", "1025"],
                ["ab", "1025"],
                ["cd", "1046"],
                ["cd", "1055"],
                ["ab", "1124"],
                ["ab", "1120"],
            ],
            ["ab", "cd"],
        ),
    ],
)
class TestSolution:
    def test_findHighAccessEmployees(
        self, access_times: List[List[str]], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.findHighAccessEmployees(
                access_times,
            )
            == output
        )
