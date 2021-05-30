const isDigit = (char) => char >= '0' && char <= '9';

const extract = (text, importPrefix, idPrefix) => {
  let searchStr = `${ importPrefix }:${ idPrefix }`;

  if (searchStr.length == 0) {
    return [];
  }

  let startIndex = 0, index, ids = [];

  while ((index = text.indexOf(searchStr, startIndex)) > -1) {
    let digitCount = searchStr.length;
    let currentString = `${ idPrefix }`;
    while (isDigit(text[index + digitCount])) {
      currentString += text[index + digitCount];
      digitCount++;
    }

    ids.push(currentString);
    startIndex = index + searchStr.length;
  }

  return [...new Set(ids)];
}

export default { extract };