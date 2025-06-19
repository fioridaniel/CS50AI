from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    Or(AKnave, AKnight), # sou apenas um dos dois
    Not(And(AKnave, AKnight)), # nao posso ser os dois ao mesmo tempo
    Biconditional(AKnight, And(AKnight, AKnave)) # A sera um knight se e somente se A for knight e knave

)

"""
    resposta:

    com certeza um dos dois nao eh um knave. knaves sempre mentem.
    se um dois dois nao eh um knave, entao um deles eh um knight.
    isso implica que B eh um knight e A eh um knave.
"""

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    
    # regra basica (so pode ser um dos dois)
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),

    # negar fala da knave
    Not(And(AKnave, BKnave)),

    # a so vai ser um cavaleiro se a fala for verdade => contradicao. logo, A eh um knave. 
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    # regra basica (so pode ser um dos dois)
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),

    # A so vai ser um cavaleiro se A e B forem
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B so vai ser um cavaleiro se nao for A e B 
    Biconditional(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))) )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # regra basica (so pode ser um dos dois)
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),


    Biconditional(AKnave, Not(Or(AKnight, AKnave))),

    Biconditional(BKnight, AKnave),    

    Biconditional(CKnave, BKnight),

    Biconditional(AKnight, CKnight)

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
 