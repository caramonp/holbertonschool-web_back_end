export default function createReportObject(employeesList) {
  return ({
    allEmployees: employeesList,
    getNumberOfDepartments: (members) => Object.keys(members).length,
  });
}
