class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
        
question_prompts = [
    "What colour are tree trunks? \na) red\nb) blue\nc) brown\n\nAnswer: ", 
    "What colour are fire trucks? \na) red\nb) purple\nc) yellow\n\nAnswer: ",
    "What colour are clouds? \na) cyan\nb) white\nc) red\n\nAnswer: ",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got " + str(score) + " out of " + str(len(questions)) + " right!")
        
run_test(questions)
