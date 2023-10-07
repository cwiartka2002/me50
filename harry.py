from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

structure_info = And(Or(AKnight, AKnave), Or(BKnave, BKnight))
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(And(AKnave, BKnight), And(AKnight, BKnave)),  # A must be either a knight or a knave
    Implication(AKnight, And(AKnight, AKnave)),  # If A is a knight, he speaks the truth
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a knave, he lies
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(Or(And(AKnave, BKnight), And(AKnight, BKnave)),

                 Implication(AKnave, Not(And(AKnave,BKnave))),
                 Implication(AKnight, And(AKnave, BKnave))

                 )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
And(Or(And(AKnave, BKnight), And(AKnight, BKnave)),
Implication(AKnave, Not(Or(And(AKnight,BKnight), And(AKnave, BKnave))))),
Implication(AKnight, Or(And(AKnight,BKnight), And(AKnave, BKnave))),
Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave)))),
Implication(BKnave, Or(And(AKnave, BKnight), And(AKnight, BKnave)))



)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(
        Or(AKnight, AKnave),  # A must be either a knight or a knave
        Or(BKnight, BKnave),  # B must be either a knight or a knave
        Or(CKnight, CKnave)  # C must be either a knight or a knave
    ),
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnave, And(Not(CKnave), Not(And(AKnave,Implication(AKnight, Or(AKnight, AKnave)))))),
    Implication(BKnight, And(CKnave, And(AKnave,Implication(AKnight, Or(AKnight, AKnave))))),
    Implication(BKnight, CKnave),
    Implication(CKnight,AKnight),
    Implication(CKnave, Not(AKnight))



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
