import pytest
from q_1108_defangingAnIpAddress import Solution


@pytest.mark.parametrize(
    "address, output",
    [("1.1.1.1", "1[.]1[.]1[.]1"), ("255.100.50.0", "255[.]100[.]50[.]0")],
)
class TestSolution:
    def test_defangIPaddr(self, address: str, output: str):
        sc = Solution()
        assert (
            sc.defangIPaddr(
                address,
            )
            == output
        )
