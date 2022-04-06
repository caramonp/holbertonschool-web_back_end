export default function updateStudentGradeByCity(arrayStudents, city, newGrades) {
  const studentsCity = arrayStudents.filter((students) => students.location === city)
    .map((student) => {
      const arrayGrades = newGrades.filter((grades) => grades.studentId === student.id);
      const result = student;
      if (arrayGrades.length === 1) {
        result.grade = arrayGrades[0].grade;
      } else result.grade = 'N/A';
      return result;
    });
  return studentsCity;
}
