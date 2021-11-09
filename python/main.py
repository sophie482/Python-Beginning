# Interactive Quiz 


def main():
  # Score
  score = 0

  # Question 1
  answer1 = input("What is the capital city of France? ")
  if answer1.lower() == "paris":
    print("Correct!")
    score += 1
  else:
    print("Incorrect :(")

  # Question 2
  answer2 = input("What is the capital city of India? ")
  if answer2.lower() == "new delhi":
    print("Correct!") 
    score += 1
  else:
    print("Incorrect :(")

  # Question 3
  answer3 = input("What is the capital city of Canada? ")
  if answer3.lower() == "ottawa":
    print("Correct!")
    score += 1
  else: 
    print("Incorrect :(")

  # Question 4
  answer4 = input("What is the capital city of Tanzania? ")
  if answer4.lower() == "dodoma":
    print("Correct!") 
    score += 1
  else:
    print("Incorrect :(")

  # Question 5
  answer5 = input("What is the capital city of Brazil? ")
  if answer5.lower() == "brasilia" or answer5.lower() == "salvador" or answer5.lower() == "rio de janeiro":
    print("Correct!")
    score += 1
  else:
    print("Incorrect :(")


  # Output Score and Feedback
  if score == 0:
    print("Your score is 0/5 (0%.) ... I don't have words.")
  elif score == 1:
    print("Your score is 1/5 (20%.) You really need to study!")
  elif score == 2: 
    print("Your score is 2/5 (40%.) Think about hitting the books more often!")
  elif score == 3:
    print("Your score is 3/5 (60%.) Getting there!")
  elif score == 4:
    print("Your score is 4/5 (80%.) Great job!")
  elif score == 5: 
    print("Your score is 5/5 (100%.) Perfect! Maybe you should be a cartographer!")

main()