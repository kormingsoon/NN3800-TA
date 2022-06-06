# NN33800-TA
Two files needed to make our lives easier:

    1. unsubmittedunapproved.py
    2. exportSIPTable.js

## ExportSIPTable
*TLDR: F12 at the page of the table, copy paste the code into the console and hit enter.*

For this file, go to page of which shows all the students under you in the browser and press F12 to launch the browser console.

The function `extractStudentInformation` takes in a parameter which will be the filetype of what you want your downloaded file to be. If not specified the default file name will be `student-info.csv`.

Copy and paste the code in ExportSIPTable.js into the console and hit enter. Your download should start after.

## unsubmittedunapproved.py

### Dependencies
Run the following commands to download the dependencies needed.
- CSV module for python  

        pip install csv

- XLRD to read excel files (exact version needed to support xlxs files. Latest only works for xls file.)
  
        pip install xlrd==1.2.0 

### Things to note
This file has four variables you should be wary of:

- `filePathToCompareAgainst`: should be the file that you have downloaded with `ExportSIPTable.js`.
&nbsp;
- `masterListPath`: this **excel file** should be what Prof Huang has sent to us.
&nbsp;
- `yourName`: this field should match **exactly** is written in the excel, so double check the field as your full name may not be in the excel file)
   &nbsp;
- `isInitialObjective`: either `True` or `False`, this is mostly to filter unnecessary information as monthly report differs from initial objective. 

## Output
1. Students who did not submit their monthly report / initial objectives.
   &nbsp;
2. Email list: Example as shown below, mostly to make our lives easier for copy pasting before sending out the reminder.

        e0123456@u.nus.edu; e0123456@u.nus.edu; e0123456@u.nus.edu; e0123456@u.nus.edu;





