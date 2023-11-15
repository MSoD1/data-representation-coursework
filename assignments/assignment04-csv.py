## Write a program in python that will read a file from a repository, 

## The program should then replace all the instances of the text "Andrew" with your name

## The program should then commit those changes and push the file back to the repository.
import csv

assignment04 = open('assignment04.csv', mode='w')
assignment04_writer = csv.writer(assignment04, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

assignment04_writer.writerow(['Andrew Smith', 'Computer Science', 'Galway'])
assignment04_writer.writerow(['Andrew Meyers', 'IT', 'Cork'])

assignment04.close()
