import aocd

puzzle = aocd.models.Puzzle(year=2023, day=5)
inp = puzzle.input_data.splitlines()
example = puzzle.examples[0][0]

puzzle.answer_a = _