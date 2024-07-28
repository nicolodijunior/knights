from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

ALied = Symbol("A Lied")

ASaysIsKnightandKnave = ALied



# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Each person is either a knight or a knave.
    Or(AKnight, AKnave),
    # If a person is a Knight, it is not a knave
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(ALied, Not(AKnight)),
    # If a person is a Knave, it is not a knight
    Implication(ASaysIsKnightandKnave, ALied),
    # If lies, is a knave
    ASaysIsKnightandKnave
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
  # Each person is either a knight or a knave.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # If a person is a Knight, it is not a knave \
    Implication(AKnight, Not(AKnave)),
    Implication(BKnight, Not(BKnave)),

    # If a person is a Knave, it is not a knight 
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),

    #

)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
  AKnave, BKnight
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
