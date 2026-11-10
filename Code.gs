/**
 * Synchronizes parsed inbox RSVPs directly into the Master Operations Sheet.
 */
function syncRosterHeadcount() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Meeting_RSVPs");
  const confirmedAttendees = [
    ["Miranda Lujan", "AIAA", "kamontelongo2@miners.utep.edu", "Oct 8 - Elmont", "CONFIRMED"],
    ["Sofia I. Oaxaca", "TSPE", "sioaxaca2@miners.utep.edu", "Oct 8 - Elmont", "CONFIRMED"],
    ["Jose Emilio Piñon", "School of Pharmacy", "jepinon@miners.utep.edu", "Oct 8 - Elmont", "CONFIRMED"],
    ["Finley E. Villegas", "Criminal Justice", "fevillegas1@miners.utep.edu", "Oct 8 - Elmont", "CONFIRMED"],
    ["Natalie Nguyen", "SSHP", "nnguyen@miners.utep.edu", "Oct 8 - Elmont", "CONFIRMED"]
  ];
  
  const lastRow = sheet.getLastRow();
  sheet.getRange(lastRow + 1, 1, confirmedAttendees.length, 5).setValues(confirmedAttendees);
}
