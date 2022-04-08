export default function cleanSet(theSet, startString) {
  const newArray = [];
  if (startString) {
    theSet.forEach((element) => {
      if (element.startsWith(startString)) {
        newArray.push(element.replace('bon', ''));
      }
    });
  } else if (typeof (startString) !== 'string') {
    return ('');
  } else {
    return ('');
  }

  return (newArray.join('-'));
}
