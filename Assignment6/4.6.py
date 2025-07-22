grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(map(lambda grade: 1.05 * grade, filter(lambda grade: grade >= 60, grades)))

print(passed_with_bonus)