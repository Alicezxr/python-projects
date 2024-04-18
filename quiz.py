def quiz():
   questions = [
      "Q1. What's the captical of China? \n(a)Wuhan\n(b)Beijing\n(c)Xiamen\n",
      "Q2. What's the captical of USA? \n(a)Wuhan\n(b)Beijing\n(c)NewYork\n",
      "Q3. What's the captical of Canada? \n(a)Wuhan\n(b)Ottawa\n(c)Xiamen\n"
]
   answers = ['a', 'b', 'c']
   score = 0

   for i in range(len(questions)):
      print(questions[i])
      user_answer = input('Enter your answer: ').lower()
      if user_answer == answers[i]:
         print('Correct!')
         score += 1
      else:
         print('Incorrect!')
      print(f"Quiz completed! Your score is {score}.")  
quiz()

