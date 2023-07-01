function levenshteinDistance(a, b) {
  let matrix = Array(a.length + 1)
    .fill(0)
    .map(() => Array(b.length + 1).fill(0));

  for (let i = 0; i <= a.length; i++) {
    matrix[i][0] = i;
  }

  for (let j = 0; j <= b.length; j++) {
    matrix[0][j] = j;
  }

  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j] + 1,       // deletion
          matrix[i][j - 1] + 1,       // insertion
          matrix[i - 1][j - 1] + 1    // substitution
        );
      }
    }
  }

  return matrix[a.length][b.length];
}

function findBestCombination(words) {
  let combinations = {};

  for (let word of words) {
    let combinationLength = word.length - 1;
    for (let i = 0; i <= word.length - combinationLength; i++) {
      let combination = word.substring(i, i + combinationLength);
      combinations[combination] = (combinations[combination] || 0) + 1;
    }
  }

  return Object.keys(combinations).reduce(
    (a, b) => (combinations[a] > combinations[b] ? a : b)
  );
}

function playGame() {
  let target = 'sing';
  let words = [
    'dunes', 'able', 'acid', 'acre', 'aged', 'aide', 'akin', 'alas', 'ally',
    'also', 'alto', 'amid', 'anal', 'anna', 'anti', 'apex', 'arch', 'area',
    'army', 'atom', 'atop', 'aunt', 'aura', 'auto', 'avid', 'away', 'axis',
    'baby', 'bach', 'back', 'bail', 'bait', 'bake', 'bald', 'ball', 'band',
    'bang', 'bank', 'bare', 'bark', 'barn', 'base', 'bass', 'bath', 'bats',
    'beam', 'bean', 'beat', 'sing'
  ];

  while (words.length) {
    var guess = findBestCombination(words);

    if (guess === target) {
      console.log(`${guess} is correct!\n[${target}]`);
      return;
    }

    if (levenshteinDistance(guess, target) === 1) {
      words = words.filter((word) => levenshteinDistance(guess, word) === 1);
      break;
    }

    words = words.filter((word) => levenshteinDistance(guess, word) > 1);
    console.log(`Best combination: ${guess}\n${words.length}`);
  }

  for (let word of words) {
    console.log(`Best combination: ${guess}\n${guess} is close!\n${words.length}`);
    guess = word;

    if (guess === target) {
      console.log(`${guess} is correct!\n[${target}]`);
      return;
    }
  }

  if (!words.length) {
    return;
  }

  console.log('List is missing the correct word.');
}




playGame();
