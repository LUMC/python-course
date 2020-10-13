# Text Files

Use a text editor of your choice to create a text file with the following
content:

    ATAC
    GG

    TATATATA
    CCC

- Read the created file in Python and for each line print the line number and
its corresponding length (number of characters). Check that the outputed
length is correct (first line in the file should have a length of four). What
about the third line?

- Now instead of printing the line length, write it into another file.

linenumber=0
with open("test.txt") as f:
        lines=f.readlines()
        for line in lines:
            linenumber+=1
            print("Line: ",linenumber,line,"Length:",len(line))
            
linenumber=0
with open("test.txt") as f:
        lines=f.readlines()
        for line in lines:
            linenumber+=1
            output=("Line: ",linenumber,line,"Length:",len(line))
            with open("output.txt", "a") as file:
                print(output, file=file)
