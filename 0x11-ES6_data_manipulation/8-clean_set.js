export default function cleanSet(theSet, startString) {
  const newArray = [];
  if (typeof (startString) === 'string' && startString) {
    theSet.forEach((element) => {
      if (element.startsWith(startString)) {
        newArray.push(element.replace('bon', ''));
      }
    });
  } else {
    return ('');
  }

  return (newArray.join('-'));
}
