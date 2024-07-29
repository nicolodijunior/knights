from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

ALied = Symbol("A Lied")
BLied = Symbol("B Lied")

ASaysTrue = Symbol("A says True")
BSaysTrue = Symbol("B says True")

ASaysNothing = Symbol("A says nothing")
BSaysNothing = Symbol("B says nothing")


ASaysIsKnightandKnave = ALied
BSaysIsKnightandKnave = BLied

ASaysBothKnave = ALied
BSaysBothKnave = BLied

ASaysBothKinght = Symbol("A says both are Kinght")
BSaysBothKinght = Symbol("B says both are Kinght")

ASaysBothSame = Symbol("A says both are the same")

BSaysBothDifferent = Symbol("B says both are different")

ASaysIsknightOrKnave = Symbol("I am a Knight or a Knave")

BSaysASaidBIsKnave = Symbol("B Says: A said B is a Knave")

BSaysCIsKnave = Symbol("B says C is a Knave")

CSaysAIsKnight = Symbol("C says A is a Knight")

# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."


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

    #If someone says both are Knave, then he is lyting
    Implication(ASaysBothKnave, ALied),
    Implication(BSaysBothKnave, BLied),

    #If someone is lying, then he is a Knave
    Implication(ALied, AKnave),
    Implication(BLied, BKnave),

    #If someone says a truth, then he is a Knight
    Implication(ASaysTrue, AKnight),
    Implication(BSaysTrue, BKnight),

    #If one says another one is they are both knaves
    Implication(And(ASaysBothKnave,BSaysNothing), BKnight),

    ASaysBothKnave,
    BSaysNothing

)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(

    # Each person is either a knight or a knave.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # If a person is a Knight, it is not a knave \
    Implication(AKnight, Not(AKnave)),
    Implication(BKnight, Not(BKnave)),

    # If a person is a Knave, it is not a knight 
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),

    #If someone says both are Knave, then he is lyting
    Implication(ASaysBothKnave, ALied),
    Implication(BSaysBothKnave, BLied),

    #If someone is lying, then he is a Knave
    Implication(ALied, AKnave),
    Implication(BLied, BKnave),

    #If someone says a truth, then he is a Knight
    Implication(ASaysTrue, AKnight),
    Implication(BSaysTrue, BKnight),

    #If someone says It is when the other lied, then he is a Knight
    Implication(And(BSaysNothing,ASaysIsKnightandKnave), BKnight),

    Implication(ASaysBothSame, Or(
        Or(AKnight,BKnight), Or(ALied)
        ),),

    Implication(BSaysBothDifferent, Not(And(BKnave, AKnight))),
    Implication(And(ASaysBothSame, BSaysBothDifferent), Or(ALied, BLied)),

    Implication(And(BSaysBothDifferent, BKnight), AKnave),
    Implication(And(ASaysBothSame, AKnave), BKnave),

    ASaysBothSame,
    BSaysBothDifferent,
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which. ASaysIsknightOrKnave
# B says "A said 'I am a knave'."                                              BSaysASaidBIsKnave
# B says "C is a knave."                                                       BSaysCIsKnave
# C says "A is a knight.",                                                     CSaysAIsKnight


knowledge3 = And(

    # BSaysASaidBIsKnave - B says "C is a knave."  

    Implication(And(BSaysASaidBIsKnave, BKnight), AKnave),    

    # B says "C is a knave." - BSaysCIsKnave
    Implication(And(BSaysCIsKnave,BKnight), CKnave),                             
    Implication(And(BSaysCIsKnave,BKnave), CKnight),
    Implication(And(BSaysCIsKnave,CKnight), BKnave),
    Implication(And(BSaysCIsKnave,CKnave), BKnight),

    # C says "A is a knight." - CSaysAIsKnight

    Implication(And(CSaysAIsKnight,CKnight), AKnight),
    Implication(And(CSaysAIsKnight,CKnave), AKnave),
    Implication(And(CSaysAIsKnight,AKnight), CKnight),
    Implication(And(CSaysAIsKnight,AKnave), CKnave),

    # Each person is either a knight or a knave.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # If a person is a Knight, it is not a knave \
    Implication(AKnight, Not(AKnave)),
    Implication(BKnight, Not(BKnave)),
    Implication(CKnight, Not(CKnave)),


    # If a person is a Knave, it is not a knight 
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),
    Implication(CKnave, Not(CKnight)),

    #If someone says both are Knave, then he is lyting
    Implication(ASaysBothKnave, ALied),
    Implication(BSaysBothKnave, BLied),

    #If someone is lying, then he is a Knave
    Implication(ALied, AKnave),
    Implication(BLied, BKnave),

    #If someone says a truth, then he is a Knight
    Implication(ASaysTrue, AKnight),
    Implication(BSaysTrue, BKnight),

    #If someone says It is when the other lied, then he is a Knight
    Implication(And(BSaysNothing,ASaysIsKnightandKnave), BKnight),

    ASaysIsknightOrKnave,
    BSaysASaidBIsKnave,
    BSaysCIsKnave,
    CSaysAIsKnight,

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
