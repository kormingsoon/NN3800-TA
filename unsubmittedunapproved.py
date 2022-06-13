# pip install csv
# pip install xlrd==1.2.0 (exact version needed to support xlxs files. Latest only works for xls file.)
import csv, xlrd

# ALL THE FIELDS TO NOTICE
isInitialObjective = False
filePathToCompareAgainst = './student-info.csv' # edit this part to whichever file u are comparing against
masterListPath = "./sip_31May2022.xlsx" # list sent to us by prof
yourName = "Kor Ming Soon" # edit to your name

# submitted student names
file = open(filePathToCompareAgainst, encoding="utf8")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
submittedNames = []
unapprovedSubmissionNames = []
for studentData in csvreader:
    submittedName = studentData[1].split("\n")[0]
    submittedNames.append(submittedName) 
    if (isInitialObjective and studentData[10] != 'Approved'):
        unapprovedSubmissionNames.append([submittedName, studentData[1].split("\n")[1]])

# master list of students
workbook = xlrd.open_workbook(masterListPath)
sheet = workbook.sheet_by_index(0)

TANames = sheet.col(2)
NUSNETID = sheet.col(5)
ALLSTUDENTS = sheet.col(6)
studentsUnderYou = []
for i in range(0, len(NUSNETID)):
    if (TANames[i].value == yourName):
        studentsUnderYou.append([ALLSTUDENTS[i].value, NUSNETID[i].value])
studentsUnderYou.sort(key=lambda x: x[0])

# Actual stuff
studentsNotSubmitted = []
studentsSupervisorNotApproved = []
print(submittedNames)
for studentUnderYou in studentsUnderYou:
    studentName = studentUnderYou[0]
    if studentName not in submittedNames:
        print(studentName)
        studentsNotSubmitted.append(studentUnderYou)

# Sanity Check
if not (len(studentsUnderYou) - len(submittedNames) == len(studentsNotSubmitted)):
    print("Students Total No: ", str(len(studentsUnderYou)))
    print("Submitted Students Total No: ", str(len(submittedNames)))
    print("Unsubmitted Students Total No: ", str(len(studentsNotSubmitted)))
    print("Number does not tally.")

 # Final Tally
if isInitialObjective:
    print(str(len(unapprovedSubmissionNames)) + " Students who submitted but supervisor has not approved:")
    unapprovedStudentEmail = ""
    for i in unapprovedSubmissionNames:
        print(i[0])
        unapprovedStudentEmail += i[1][1:-1] + "; " 
    print("------")
    print("Unapproved Email List:")
    print(unapprovedStudentEmail)
    print("------------------------------------------------------------------")
print(str(len(studentsNotSubmitted)) + " Students who did not submit:")
unsubmittedStudentEmail = ""
for i in studentsNotSubmitted:
    print(i[0])
    unsubmittedStudentEmail += i[1] + "@u.nus.edu; " 
print("------")
print("Unsubmitted Email List:")
print(unsubmittedStudentEmail)
print("------")


