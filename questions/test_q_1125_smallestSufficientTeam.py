import pytest
from q_1125_smallestSufficientTeam import Solution


@pytest.mark.parametrize(
    "req_skills, people, output",
    [
        (
            ["java", "nodejs", "reactjs"],
            [["java"], ["nodejs"], ["nodejs", "reactjs"]],
            [0, 2],
        ),
        (
            ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            [
                ["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"],
            ],
            [1, 2],
        ),
    ],
)
class TestSolution:
    def test_smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.smallestSufficientTeam(
                req_skills,
                people,
            )
            == output
        )
