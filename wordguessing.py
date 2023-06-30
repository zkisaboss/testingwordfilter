def levenshtein_distance(a, b):
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        matrix[i][0] = i
    for j in range(len(b) + 1):
        matrix[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                deletion = matrix[i - 1][j] + 1
                insertion = matrix[i][j - 1] + 1
                substitution = matrix[i - 1][j - 1] + 1
                matrix[i][j] = min(deletion, insertion, substitution)

    return matrix[-1][-1]


def find_best_combination(words):
    combinations = []

    for c1 in range(ord('a'), ord('z') + 1):
        for c2 in range(ord('a'), ord('z') + 1):
            for c3 in range(ord('a'), ord('z') + 1):
                combination = chr(c1) + chr(c2) + chr(c3)
                removed_count = sum(combination in word for word in words)
                combinations.append((combination, removed_count))

    combinations.sort(key=lambda x: x[1], reverse=True)
    best_combination = combinations[0][0]
    return best_combination


def play_game():
    global words
    print(f"{words[:12]}\n{len(words)}")

    while True:
        best_combination = input("Guess: ")
        print("Best combination:", best_combination)

        if best_combination == target:
            print(f"{best_combination} is correct!\n{[target]}")
            return

        distance = levenshtein_distance(best_combination, target)
        if distance == 1:
            print(f"{best_combination} is close!")

            close_words = [word for word in words if levenshtein_distance(best_combination, word) == 1]
            words = close_words
        else:
            distant_words = [word for word in words if levenshtein_distance(best_combination, word) > 1]
            words = distant_words

        print(words[:12])
        print(len(words))


target = 'dune'
words = ['dunes', 'able', 'acid', 'acre', 'aged', 'aide', 'akin', 'alas', 'ally', 'also', 'alto', 'amid', 'anal', 'anna', 'anti', 'apex']

find_best_combination(words)
play_game()
