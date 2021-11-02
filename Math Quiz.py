# Maths Quiz
# Aleksis Vanags
# 02/11/2021

from random import randint as r, choice as c

operators = ["+", "-", "*", "/"]


def main():
    """Starts the quiz"""
    score = 0
    name = input("Enter your name:   ")
    difficulty = input("Choose your difficulty:\nEasy\nMedium\nHard\n")
    for _ in range(20):
        package = createQuestion(difficulty.lower())
        answer = makeQuestion(package[0], package[1])
        answerInput = input("Enter your answer:   ")
        if answerInput == answer:
            print("You are correct!")
            score += 1
        else:
            print("You are incorrect!")
    with open(f"scores{difficulty}.txt", "a") as file:
        file.write("Username: " + name + "# Score: " + str(score) + "/20 " + str((score / 20) * 100) + "%\n")
    again = input("Do you want to see the top 10?\n").lower()
    if again == "y":
        displayTopTen(difficulty)


def createQuestion(difficulty):
    """Creates each question in the quiz one at a time"""
    if difficulty == "easy":
        multiplier = 1
    elif difficulty == "medium":
        multiplier = 3
    elif difficulty == "hard":
        multiplier = 7
    operator = c(operators)
    num1 = multiplier * r(1, 100)
    num2 = multiplier * r(1, 100)
    if operator == "+":
        answer = num1 + num2
        question = str(num1) + " " + operator + " " + str(num2)
    elif operator == "-":
        answer = num1 - num2
        question = str(num1) + " " + operator + " " + str(num2)
    elif operator == "*":
        answer = num1 * num2
        question = str(num1) + " " + operator + " " + str(num2)
    else:
        num2 = r(1, 100)
        num1 = num2 * r(1, 9)
        answer = num1 / num2
        question = str(multiplier * num1) + " " + operator + " " + str(multiplier * num2)
    return [question, answer]


def makeQuestion(question, answer):
    """Finalizes and cleans up the question creation stage"""
    questionToDisplay = question.split()
    questionToDisplay.append(" = ")
    questionToDisplay.append(answer)
    while True:
        toRemove = r(0, len(questionToDisplay) - 1)
        if questionToDisplay[toRemove] != " = ":
            answerToEnter = questionToDisplay[toRemove]
            questionToDisplay[toRemove] = "??"
            break
    print(*questionToDisplay)
    return answerToEnter


def displayTopTen(difficulty):
    """Displays the top ten results stored in the txt file for the specified difficulty"""
    with open(f"scores{difficulty}.txt", "r") as file:
        scores = []
        users = []
        userScoreDict = {}
        for line in file:
            score = line.split()
            for word in score:
                for letter in word:
                    if letter == "#":
                        users.append(word[:-1])
                    if letter == "%":
                        scores.append(float(word[:-1]))
    for x, _ in enumerate(scores):
        userScoreDict[users[x]] = scores[x]
    userScoreDict = sorted(userScoreDict.items(), key=lambda x: x[1], reverse=True)
    if len(scores) >= 10:
        for x in range(10):
            print("Username:", userScoreDict[x][0], "Score:", userScoreDict[x][1] * 0.2, "/20", userScoreDict[x][1], "%")
    else:
        for x in range(len(scores)):
            print("Username:", userScoreDict[x][0], "Score:", userScoreDict[x][1] * 0.2, "/20", userScoreDict[x][1], "%")


if __name__ == "__main__":
    main()
