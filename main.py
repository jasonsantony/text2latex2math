from latex2sympy2 import latex2sympy
from sympy import simplify
import re


def evaluate(text):
    """
    Extract LaTeX math snippets from a given string, convert them to sympy expressions, and evaluate them.

    Args:
    text (str): The input string containing LaTeX math snippets.

    Returns:
    fully_evaluated_expressions: A list of evaluated sympy expressions.
    """
    # Regular expression to match inline and display math snippets
    pattern = r"(\$\$.*?\$\$|\$.*?\$)"
    snippets = re.findall(pattern, text, re.DOTALL)
    expressions = [latex2sympy(snippet.strip("$")) for snippet in snippets]
    partially_evaluated_expressions = [simplify(expr) for expr in expressions]
    # Evaluate advanced expressions with calculus etc.
    fully_evaluated_expressions = [
        expr.doit() for expr in partially_evaluated_expressions
    ]

    return fully_evaluated_expressions


text = r"""
    hello this is not latex
    $\frac{1}{2}x^2 + 3x + 4$
    $$\int x^2 dx$$
    $\sum_{n=1}^{\infty} \frac{1}{n^2}$
    $$4 + 4$$
    this is also not latex
"""

print(evaluate(text))
