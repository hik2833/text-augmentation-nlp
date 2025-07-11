import os
import random

# Simple synonym dictionary for demonstration
SYNONYMS = {
    "quick": ["fast", "swift", "speedy"],
    "brown": ["tan", "umber", "chocolate"],
    "fox": ["animal", "creature"],
    "jumps": ["leaps", "bounds"],
    "lazy": ["idle", "sluggish"],
    "dog": ["canine", "puppy"],
    "natural": ["innate", "inherent"],
    "language": ["linguistic", "speech"],
    "processing": ["handling", "analysis"],
    "artificial": ["synthetic", "man-made"],
    "intelligence": ["smartness", "cognition"],
    "data": ["information", "details"],
    "augmentation": ["expansion", "enhancement"],
    "improve": ["enhance", "boost"],
    "model": ["framework", "system"],
    "robustness": ["strength", "resilience"],
    "helps": ["assists", "supports"],
    "branch": ["division", "field"],
}

def replace_synonyms(line):
    words = line.strip().split()
    new_words = []
    for word in words:
        key = word.lower().strip(".,!?")
        if key in SYNONYMS:
            synonym = random.choice(SYNONYMS[key])
            # Preserve capitalization if needed
            if word[0].isupper():
                synonym = synonym.capitalize()
            new_words.append(synonym)
        else:
            new_words.append(word)
    return " ".join(new_words)

def augment_file(filename):
    new_filename = filename.replace(".txt", "_augmented.txt")
    with open(filename, 'r', encoding='utf-8') as f_in, open(new_filename, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            augmented_line = replace_synonyms(line)
            f_out.write(augmented_line + "\n")
    print(f"Augmented file saved as: {new_filename}")

def main():
    for filename in os.listdir():
        if filename.endswith(".txt") and "augmented" not in filename:
            augment_file(filename)

if __name__ == "__main__":
    main()
