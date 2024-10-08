import pytest
from q_1324_printWordsVertically import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("HOW ARE YOU", ["HAY", "ORO", "WEU"]),
        ("TO BE OR NOT TO BE", ["TBONTB", "OEROOE", "   T"]),
        ("CONTEST IS COMING", ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]),
    ],
)
class TestSolution:
    def test_printVertically(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.printVertically(
                s,
            )
            == output
        )
