import pytest
from q_0824_goatLatin import Solution


@pytest.mark.parametrize(
    "sentence, output",
    [
        ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
        (
            "The quick brown fox jumped over the lazy dog",
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        ),
    ],
)
class TestSolution:
    def test_toGoatLatin(self, sentence: str, output: str):
        sc = Solution()
        assert (
            sc.toGoatLatin(
                sentence,
            )
            == output
        )
