import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 5) : 
    Application_No,HighSchool_GPA,Physics_Marks,Chem_Marks,Biology_Marks = datalist

    # print intermediate key-value pairs to standard output
    print(Application_No,"\t",Physics_Marks)