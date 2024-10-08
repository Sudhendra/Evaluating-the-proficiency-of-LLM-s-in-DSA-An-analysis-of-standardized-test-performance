import pytest
from q_0093_restoreIpAddresses import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ],
)
class TestSolution:
    def test_restoreIpAddresses(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.restoreIpAddresses(
                s,
            )
            == output
        )
