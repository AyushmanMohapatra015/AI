import random

# Possible human-like responses
human_replies = {
    "how are you": [
        "Pretty good actually, just relaxing.",
        "Doing alright, a little tired though.",
        "I'm fine, just busy with some work."
    ],

    "what do you like": [
        "I enjoy music and going out with friends.",
        "Mostly sports and movies.",
        "Reading and gaming are fun for me."
    ],

    "what is 6+4": [
        "That should be 10.",
        "Easy, it's 10.",
        "Hmm... 10 I think."
    ]
}

# Possible AI-like responses
ai_replies = {
    "how are you": [
        "System status: operating normally.",
        "All processes are functioning correctly."
    ],

    "what do you like": [
        "I do not experience personal preferences.",
        "I am not capable of hobbies."
    ],

    "what is 6+4": [
        "The computed result equals 10.",
        "Calculation result: 10."
    ]
}


def generate_answer(question, agent):
    q = question.lower()

    if agent == "human":
        if q in human_replies:
            return random.choice(human_replies[q])
        return "I'm not sure about that question."

    else:
        if q in ai_replies:
            return random.choice(ai_replies[q])
        return "Input not recognized."


def run_turing_test():

    score = 0
    rounds = 3

    for i in range(rounds):

        print("\nRound", i + 1)
        responder = random.choice(["human", "ai"])

        question = input("Judge asks: ")

        answer = generate_answer(question, responder)

        print("Response:", answer)

        guess = input("Is it human or ai? ").lower()

        if guess == responder:
            print("Correct guess!")
            score += 1
        else:
            print("Wrong guess!")

    print("\nFinal Score:", score, "/", rounds)


run_turing_test()
