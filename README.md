**Hostel Management System using Flask**

A smart allocation system built upon the tools of Data science and analytics for a college.

This idea was taken from a problem statement provided for Codebreak 1.0 hackathon.

This app allocates rooms based on six aspects:

1. Name
2. Age
3. Branch
4. Roll number
5. Gender
6. Room number

This app considers two cases for room allotment:

1. When the hostel is empty i.e. no room is allotted to any student initially,  in this case rooms are allotted to an unordered list of students on the basis of age and branch of study. This incorporates data science tools.
2. When some of the rooms are already filled, then new room is allotted on the basis of First come First serve basis. If a student leaves the hostel earlier than scheduled than that particular room is allocated if the age and branch of the new student matches the corresponding aspects of the student who has left. Otherwise, a new room is allocated.