export default function getStudentIdsSum(students) {
  const sumId = students.reduce(
    (previousValue, currentValue) => previousValue + currentValue.id,
    0,
  );
  return sumId;
}
