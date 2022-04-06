export default function getListStudentIds(array) {
  let arrayID = [];

  if (Array.isArray(array)) {
    arrayID = array.map((information) => information.id);
    return arrayID;
  } return arrayID;
}
