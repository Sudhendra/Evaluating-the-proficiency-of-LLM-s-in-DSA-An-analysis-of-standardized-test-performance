class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expression):
            terms = expression.split('+')
            result = [0, 0]  # Coefficient of x and constant term
            for term in terms:
                if '-' in term:
                    sub_terms = term.split('-')
                    if sub_terms[0] == '':
                        sub_terms = sub_terms[1:]
                        result[1] -= int(sub_terms[0])
                    else:
                        result[0] += int(sub_terms[0])
                        for sub_term in sub_terms[1:]:
                            result[1] -= int(sub_term)
                else:
                    if 'x' in term:
                        if term == 'x':
                            result[0] += 1
                        else:
                            result[0] += int(term[:-1])
                    else:
                        result[1] += int(term)
            return result

        left, right = equation.split('=')
        left_result = evaluate(left)
        right_result = evaluate(right)

        x_coef = left_result[0] - right_result[0]
        const = right_result[1] - left_result[1]

        if x_coef == 0 and const == 0:
            return "Infinite solutions"
        if x_coef == 0 and const != 0:
            return "No solution"
        
        return "x=" + str(const // x_coef)