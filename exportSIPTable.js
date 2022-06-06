
function extractStudentInformation(fileName) {
    var studentsData = document.querySelectorAll('table tr');
    console.save(studentsData, fileName);
}

console.save = function (studentsData, fileName) {

    if (!fileName) fileName = 'student-info.csv';
   
    var csv = [];
    for (var i = 1; i < studentsData.length; i++) { // starts from 1 to ignore legend table
        var studentData = [], columnInfo = studentsData[i].querySelectorAll("td, th");
        for (var j = 0; j < columnInfo.length; j++) {
            var toParseString = "\"" + columnInfo[j].innerText + "\"";
            studentData.push(toParseString.replaceAll('-', 'Bullet: '));
        }
        csv.push(studentData.join(","));        
    }
    
    // copied off some stackexchange article
    var blob = new Blob([csv.join("\n")], { type: 'text/csv'});
    creationEvent = document.createEvent('MouseEvents');
    aReference = document.createElement('a');

    aReference.download = fileName
    aReference.href = window.URL.createObjectURL(blob)
    aReference.dataset.downloadurl = ['text/csv', aReference.download, aReference.href].join(':')
    creationEvent.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    aReference.dispatchEvent(creationEvent)
}

extractStudentInformation();