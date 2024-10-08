import pytest
from q_0433_minimumGeneticMutation import Solution


@pytest.mark.parametrize(
    "startGene, endGene, bank, output",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
    ],
)
class TestSolution:
    def test_minMutation(
        self, startGene: str, endGene: str, bank: List[str], output: int
    ):
        sc = Solution()
        assert (
            sc.minMutation(
                startGene,
                endGene,
                bank,
            )
            == output
        )
