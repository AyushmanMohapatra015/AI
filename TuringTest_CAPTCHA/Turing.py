import random

human_answers = {
    "hello": ["Hey there!", "Hi! How's it going?", "Hello!"],
    "what is 5+3": ["That's 8.", "Pretty sure it's 8.", "8, easy!"],
    "do you like music": ["Yeah, I listen to music a lot.", "Music is great!"]
}

ai_answers = {
    "hello": ["Greetings.", "Hello. I acknowledge your message."],
    "what is 5+3": ["The result equals 8.", "Calculation output: 8."],
    "do you like music": ["I do not possess preferences.", "I cannot experience music."]
}

def reply(question, agent):
    q = question.lower()

    if agent == "human":
        if q in human_answers:
            return random.choice(human_answers[q])
        return "Hmm, I am not sure."

    else:
        if q in ai_answers:
            return random.choice(ai_answers[q])
        return "Input not understood."


def turing_test():

    rounds = 3
    correct = 0

    for i in range(rounds):

        print("\nRound", i+1)

        agent = random.choice(["human", "ai"])

        question = input("Judge asks: ")

        response = reply(question, agent)

        print("Response:", response)

        guess = input("Your guess (human/ai): ").lower()

        if guess == agent:
            print("Correct guess.")
            correct += 1
        else:
            print("Wrong guess.")

    print("\nJudge guessed correctly", correct, "out of", rounds)

    if correct >= 2:
        print("Judge successfully distinguished the AI from the human.")
    else:
        print("AI passed the Turing Test. The judge could not reliably tell.")


turing_test()
