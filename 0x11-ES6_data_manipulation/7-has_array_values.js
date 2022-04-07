export default function hasValuesFromArray(setElement, array) {
  const sett = array.map((value) => setElement.has(value))
    .reduce((prev, current) => (!!((prev && current))));
  return sett;
}
