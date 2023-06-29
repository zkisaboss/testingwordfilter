def levenshtein_distance(a, b):
    # Initialize a matrix of size (len(s1)+1) x (len(s2)+1) with all values set to 0
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(a) + 1):
        matrix[i][0] = i
    for j in range(len(b) + 1):
        matrix[0][j] = j

    # Compute the Levenshtein distance
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,       # deletion
                    matrix[i][j - 1] + 1,       # insertion
                    matrix[i - 1][j - 1] + 1    # substitution
                )

    # Return the Levenshtein distance (last element in the matrix)
    return matrix[-1][-1]


def find_best_combination(words):
    combinations = []

    for c1 in range(ord('a'), ord('z') + 1):
        for c2 in range(ord('a'), ord('z') + 1):
            for c3 in range(ord('a'), ord('z') + 1):
                combination = chr(c1) + chr(c2) + chr(c3)
                removed_count = 0

                for word in words:
                    if combination in word:
                        removed_count += 1

                combinations.append((combination, removed_count))

    # Sort the combinations based on the removed count in descending order
    combinations.sort(key=lambda x: x[1], reverse=True)

    # Extract the best combination (first element) from the sorted list
    best_combination = combinations[0][0]

    return best_combination




def play_game():
    global words
    print(words[:12])

    while True:
        print("Best combination:", find_best_combination(words))
        guess = find_best_combination(words)
        
        if guess == target:
            print(f"{guess} is correct!\n{[target]}")
            return

        if levenshtein_distance(guess, target) == 1:
            print(f"{guess} is close!")

            close_words = []
            for word in words:
                if levenshtein_distance(guess, word) == 1:
                    close_words.append(word)
            words = close_words
        else:
            distant_words = []
            for word in words:
                if levenshtein_distance(guess, word) > 1:
                    distant_words.append(word)
            words = distant_words
        print(words[:12])
        print(len(words))

target = 'dune'
words = ['dunes', 'able', 'acid', 'acre', 'aged', 'aide', 'akin', 'alas', 'ally', 'also', 'alto', 'amid', 'anal', 'anna', 'anti', 'apex', 'arch', 'area', 'army', 'atom', 'atop', 'aunt', 'aura', 'auto', 'avid', 'away', 'axis', 'baby', 'bach', 'back', 'bail', 'bait', 'bake', 'bald', 'ball', 'band', 'bang', 'bank', 'bare', 'bark', 'barn', 'base', 'bass', 'bath', 'bats', 'beam', 'bean', 'beat', 'beck', 'beef', 'been', 'beer', 'bell', 'belt', 'bend', 'bent', 'best', 'beta', 'beth', 'bias', 'bike', 'bill', 'bind', 'bird', 'bite', 'blew', 'bloc', 'blog', 'blow', 'blue', 'blur', 'boat', 'body', 'boil', 'bold', 'bolt', 'bomb', 'bond', 'bone', 'book', 'boom', 'boon', 'boot', 'bore', 'born', 'boss', 'both', 'bout', 'bowl', 'brad', 'bred', 'brew', 'brow', 'buck', 'bulb', 'bulk', 'bull', 'bump', 'burn', 'bury', 'bush', 'bust', 'busy', 'butt', 'buzz', 'cafe', 'cage', 'cake', 'calf', 'call', 'calm', 'came', 'camp', 'cane', 'cape', 'card', 'care', 'carl', 'carr', 'cart', 'case', 'cash', 'cast', 'cave', 'cell', 'cent', 'chad', 'chap', 'chat', 'chef', 'chic', 'chin', 'chip', 'chop', 'cite', 'city', 'clad', 'clan', 'clay', 'clip', 'club', 'clue', 'coal', 'coat', 'coca', 'code', 'coil', 'coin', 'coke', 'cola', 'cold', 'cole', 'come', 'cone', 'conn', 'cook', 'cool', 'cope', 'copy', 'cord', 'core', 'cork', 'corn', 'cost', 'coup', 'cove', 'crap', 'crew', 'crop', 'crow', 'cube', 'cult', 'curb', 'cure', 'cute', 'dale', 'dame', 'damn', 'damp', 'dare', 'dark', 'dash', 'data', 'date', 'dawn', 'days', 'dead', 'deaf', 'deal', 'dean', 'dear', 'debt', 'deck', 'deed', 'deep', 'deer', 'dell', 'demo', 'dent', 'deny', 'desk', 'dial', 'dice', 'dick', 'diet', 'dire', 'dirt', 'disc', 'dish', 'disk', 'dive', 'dock', 'does', 'dole', 'doll', 'dome', 'done', 'doom', 'door', 'dose', 'dove', 'down', 'drag', 'draw', 'drew', 'drop', 'drug', 'drum', 'dual', 'duck', 'duff', 'duke', 'dull', 'duly', 'dumb', 'dump', 'dune', 'dusk', 'dust', 'duty', 'each', 'earn', 'ease', 'east', 'easy', 'eats', 'echo', 'edge', 'edit', 'else', 'envy', 'epic', 'euro', 'even', 'ever', 'evil', 'exam', 'exit', 'expo', 'eyed', 'face', 'fact', 'fade', 'fail', 'fair', 'fake', 'fall', 'fame', 'fare', 'farm', 'fast', 'fate', 'fear', 'feat', 'feed', 'feel', 'feet', 'fell', 'felt', 'file', 'fill', 'film', 'find', 'fine', 'fire', 'firm', 'fish', 'fist', 'five', 'flag', 'flat', 'fled', 'flee', 'flew', 'flex', 'flip', 'flow', 'flux', 'foam', 'foil', 'fold', 'folk', 'fond', 'font', 'food', 'fool', 'foot', 'ford', 'fore', 'fork', 'form', 'fort', 'foul', 'four', 'free', 'frog', 'from', 'fuck', 'fuel', 'full', 'fund', 'fury', 'fuse', 'fuss', 'gain', 'gala', 'gale', 'gall', 'game', 'gang', 'gate', 'gave', 'gaze', 'gear', 'gene', 'gift', 'gill', 'girl', 'give', 'glad', 'glen', 'glow', 'glue', 'goal', 'goat', 'goes', 'gold', 'golf', 'gone', 'good', 'gore', 'gown', 'grab', 'gram', 'gray', 'grew', 'grey', 'grid', 'grim', 'grin', 'grip', 'grow', 'gulf', 'guru', 'hail', 'hair', 'hale', 'half', 'hall', 'halt', 'hand', 'hang', 'hank', 'hard', 'harm', 'hart', 'hate', 'haul', 'have', 'hawk', 'head', 'heal', 'heap', 'heat', 'heel', 'heir', 'held', 'hell', 'helm', 'help', 'herb', 'herd', 'here', 'hero', 'hers', 'hide', 'high', 'hike', 'hill', 'hint', 'hire', 'hold', 'hole', 'holt', 'holy', 'home', 'hood', 'hook', 'hope', 'horn', 'hose', 'host', 'hour', 'huge', 'hull', 'hung', 'hunt', 'hurt', 'hype', 'icon', 'idea', 'idle', 'idol', 'inch', 'info', 'into', 'iris', 'iron', 'isle', 'item', 'jack', 'jail', 'jake', 'jane', 'java', 'jazz', 'jean', 'jeep', 'jill', 'joey', 'john', 'join', 'joke', 'josh', 'jump', 'junk', 'jury', 'just', 'keen', 'keep', 'kemp', 'kent', 'kept', 'khan', 'kick', 'kill', 'kind', 'king', 'kirk', 'kiss', 'kite', 'knee', 'knew', 'knit', 'knot', 'know', 'kohl', 'Kyle', 'lace', 'lack', 'lady', 'laid', 'lake', 'lamb', 'lamp', 'land', 'lane', 'lang', 'last', 'late', 'lava', 'lawn', 'lazy', 'lead', 'leaf', 'leak', 'lean', 'leap', 'left', 'lend', 'lens', 'lent', 'less', 'lest', 'levy', 'lied', 'lien', 'life', 'lift', 'like', 'lily', 'limb', 'lime', 'limp', 'line', 'link', 'lion', 'list', 'live', 'load', 'loan', 'lock', 'loft', 'logo', 'lone', 'long', 'look', 'loop', 'lord', 'lose', 'loss', 'lost', 'loud', 'love', 'luck', 'lump', 'lung', 'lure', 'lush', 'lust', 'made', 'maid', 'mail', 'main', 'make', 'male', 'mall', 'mama', 'many', 'marc', 'mark', 'mart', 'mask', 'mass', 'mate', 'matt', 'mayo', 'maze', 'mead', 'meal', 'mean', 'meat', 'meet', 'Mega', 'melt', 'memo', 'menu', 'mere', 'mesa', 'mesh', 'mess', 'mice', 'mick', 'mike', 'mild', 'mile', 'milk', 'mill', 'mind', 'mine', 'mini', 'mint', 'miss', 'mist', 'mock', 'mode', 'mold', 'monk', 'mood', 'moon', 'more', 'moss', 'most', 'move', 'much', 'must', 'myth', 'nail', 'name', 'navy', 'near', 'neat', 'neck', 'need', 'nest', 'news', 'next', 'nice', 'nick', 'nine', 'node', 'none', 'noon', 'norm', 'nose', 'note', 'nova', 'nude', 'nuts', 'oath', 'obey', 'odds', 'odor', 'okay', 'once', 'only', 'onto', 'open', 'oral', 'otto', 'ours', 'oval', 'oven', 'over', 'pace', 'pack', 'pact', 'page', 'paid', 'pain', 'pair', 'pale', 'palm', 'papa', 'para', 'park', 'part', 'pass', 'past', 'path', 'peak', 'peat', 'peck', 'peel', 'peer', 'pest', 'pick', 'pier', 'pike', 'pile', 'pill', 'pine', 'pink', 'pint', 'pipe', 'pity', 'plan', 'play', 'plea', 'plot', 'plug', 'plus', 'poem', 'poet', 'pole', 'poll', 'polo', 'poly', 'pond', 'pony', 'pool', 'poor', 'pope', 'pork', 'port', 'pose', 'post', 'pour', 'pray', 'prep', 'prey', 'prof', 'prop', 'pull', 'pulp', 'pump', 'punk', 'pure', 'push', 'quid', 'quit', 'quiz', 'race', 'rack', 'rage', 'raid', 'rail', 'rain', 'ramp', 'rang', 'rank', 'rape', 'rare', 'rash', 'rate', 'rave', 'read', 'real', 'reap', 'rear', 'reed', 'reef', 'reel', 'rely', 'rent', 'rest', 'rice', 'rich', 'rick', 'ride', 'ring', 'riot', 'ripe', 'rise', 'risk', 'rite', 'ritz', 'road', 'roar', 'rock', 'rode', 'role', 'roll', 'roof', 'room', 'root', 'rope', 'rose', 'ruby', 'rude', 'ruin', 'rule', 'rush', 'rust', 'ruth', 'sack', 'safe', 'saga', 'sage', 'said', 'sail', 'sake', 'sale', 'salt', 'same', 'sand', 'sang', 'sank', 'save', 'scan', 'scar', 'scot', 'seal', 'seat', 'seed', 'seek', 'seem', 'seen', 'self', 'sell', 'semi', 'send', 'sent', 'sept', 'sexy', 'shah', 'shed', 'ship', 'shit', 'shoe', 'shop', 'shot', 'show', 'shut', 'sick', 'side', 'sigh', 'sign', 'silk', 'sing', 'sink', 'site', 'size', 'skin', 'skip', 'slab', 'slam', 'slap', 'slid', 'slim', 'slip', 'slot', 'slow', 'snap', 'snow', 'soap', 'soar', 'soda', 'sofa', 'soft', 'soil', 'sold', 'sole', 'solo', 'some', 'song', 'soon', 'sore', 'sort', 'soul', 'soup', 'sour', 'span', 'spin', 'spit', 'spot', 'spun', 'spur', 'star', 'stay', 'stem', 'step', 'stir', 'stop', 'such', 'suck', 'suit', 'sung', 'sunk', 'sure', 'surf', 'swan', 'swap', 'sway', 'swim', 'tack', 'tail', 'take', 'tale', 'talk', 'tall', 'tank', 'tape', 'taps', 'task', 'taxi', 'team', 'tear', 'tech', 'teen', 'tell', 'tend', 'tent', 'term', 'test', 'text', 'than', 'that', 'them', 'then', 'they', 'thin', 'this', 'thou', 'thus', 'tick', 'tide', 'tidy', 'tier', 'tile', 'till', 'tilt', 'time', 'tiny', 'tire', 'toby', 'told', 'toll', 'tomb', 'tone', 'tony', 'took', 'tool', 'tops', 'tore', 'torn', 'tort', 'toss', 'tour', 'town', 'trap', 'tray', 'tree', 'trek', 'trim', 'trio', 'trip', 'troy', 'true', 'tube', 'tuck', 'tuna', 'tune', 'turf', 'turn', 'twin', 'type', 'ugly', 'unit', 'upon', 'urge', 'used', 'user', 'vain', 'vary', 'vast', 'veil', 'vein', 'verb', 'very', 'vest', 'veto', 'vice', 'view', 'vine', 'visa', 'void', 'vote', 'wade', 'wage', 'wait', 'wake', 'walk', 'wall', 'want', 'ward', 'ware', 'warm', 'warn', 'wary', 'wash', 'watt', 'wave', 'ways', 'weak', 'wear', 'weed', 'week', 'well', 'went', 'were', 'west', 'what', 'when', 'whip', 'whom', 'wide', 'wife', 'wild', 'will', 'wind', 'wine', 'wing', 'wipe', 'wire', 'wise', 'wish', 'with', 'woke', 'wolf', 'wood', 'wool', 'word', 'wore', 'work', 'worm', 'worn', 'wrap', 'yang', 'yard', 'yarn', 'yeah', 'year', 'your', 'yuan', 'zero', 'zinc', 'zone', 'zoom']

find_best_combination(words)
play_game()
