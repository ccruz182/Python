def filter_odds(num):
    return num % 2 != 0

def filter_lowers(ch: str):
    return ch.islower()

def squarizer(num: int):
    return pow(num, 2)

def to_grade(calification: int) -> str:
    grade = 'A'
    if (calification < 90 and calification > 80):
        grade = 'B'
    elif (calification < 80 and calification > 70):
        grade = 'C'
    elif (calification < 70 and calification > 65):
        grade = 'D'
    elif (calification < 65 and calification >= 60):
        grade = 'E'
    elif (calification < 60):
        grade = 'F'

    return grade




def main():
    nums = (1, 8, 20, 4050, 10, -3)
    chars = "cmcdmkeEcdmP"
    grades = (81, 90, 100, 40, 99, 77)

    # Filter => Remove items
    odds = list(filter(filter_odds, nums))
    print("Filter:", odds)

    # Filter => Non-numeric sequence
    lowers = list(filter(filter_lowers, chars))
    print("Lowers:", lowers)

    # Map
    squares = list(map(squarizer, nums))
    print("Squares:", squares)

    # Sort
    grades = list(map(to_grade, sorted(grades)))
    print("Grades:", grades)


if __name__ == "__main__":
    main()