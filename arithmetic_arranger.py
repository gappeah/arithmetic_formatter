def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(parts[0]), len(parts[2])) + 2
        first_line += parts[0].rjust(width) + "    "
        second_line += parts[1] + parts[2].rjust(width - 1) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if parts[1] == '+':
                answer = int(parts[0]) + int(parts[2])
            else:
                answer = int(parts[0]) - int(parts[2])
            answer_line += str(answer).rjust(width) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()

    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems
