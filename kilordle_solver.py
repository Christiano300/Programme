import json

with open('files/wordles.json', 'r') as f:
    WORDLES = json.load(f)

with open('files/words.json', 'r') as f:
    ALL_WORDS = json.load(f)

target = set()
covered = set()
words = []

for word in WORDLES:
    for i, letter in enumerate(word):
        pos_letter = str(i) + letter
        target.add(pos_letter)

print(target)
print(f"Total unique position-letter combinations: {len(target)}")

while len(covered) < len(target):
    best_word = None
    best_new_covers = set()

    for word in ALL_WORDS:
        new_covers = set()
        for i, letter in enumerate(word):
            pos_letter = str(i) + letter
            if pos_letter in target and pos_letter not in covered:
                new_covers.add(pos_letter)
        
        new_covers.difference_update(covered)

        if len(new_covers) > len(best_new_covers):
            best_new_covers = new_covers
            best_word = word
            if len(best_new_covers) == 5:
                break

    if best_word is None:
        break

    
    print(f"Selected word: {best_word}, covers {len(best_new_covers)} new combinations.")
    print(f"Total covered: {len(covered) + len(best_new_covers)} / {len(target)}")

    words.append(best_word)
    covered.update(best_new_covers)
    ALL_WORDS.remove(best_word)

print("\nFinal selected words:")
for word in words:
    print(word)