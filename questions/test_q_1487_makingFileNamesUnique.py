import pytest
from q_1487_makingFileNamesUnique import Solution


@pytest.mark.parametrize(
    "names, output",
    [
        (["pes", "fifa", "gta", "pes(2019)"], ["pes", "fifa", "gta", "pes(2019)"]),
        (["gta", "gta(1)", "gta", "avalon"], ["gta", "gta(1)", "gta(2)", "avalon"]),
        (
            ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"],
            ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"],
        ),
    ],
)
class TestSolution:
    def test_getFolderNames(self, names: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.getFolderNames(
                names,
            )
            == output
        )
