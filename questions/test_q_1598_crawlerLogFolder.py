import pytest
from q_1598_crawlerLogFolder import Solution


@pytest.mark.parametrize(
    "logs, output",
    [
        (["d1/", "d2/", "../", "d21/", "./"], 2),
        (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
        (["d1/", "../", "../", "../"], 0),
    ],
)
class TestSolution:
    def test_minOperations(self, logs: List[str], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                logs,
            )
            == output
        )
