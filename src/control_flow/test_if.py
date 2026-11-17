"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_nested_if_statement():
    """A second condition can be checked only after the first one passes."""

    has_ticket = True
    age = 16
    admission = ''

    if has_ticket:
        if age < 18:
            admission = 'Admit with a guardian'
        else:
            admission = 'Admit'
    else:
        admission = 'Ticket required'

    assert admission == 'Admit with a guardian'


def test_multiple_elif_score_ranges():
    """Check score ranges from highest to lowest to select one result."""

    cases = [(75, 'B'), (60, 'C')]

    for score, expected_grade in cases:
        if score >= 90:
            grade = 'A'
        elif score >= 75:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        else:
            grade = 'F'

        assert grade == expected_grade
