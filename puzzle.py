#Project 5 Puzzle Program
#
#Name: Rohith Dara
#Instructor: S.Einakian
#Section: 01

import sys

'''
Pseudocode for Main Puzzle
Try to open the second argument of the command line
If the image file won't open, print the unable to open message and exit
Open and write the first 3 lines of the input file to the output file
Create a list of all the pixels
Update the pixels with the update rgb function
Write each of the rgb values of each pixel on separate lines to the output file
'''
#This function runs the puzzle function
#->
def main():
   argval = sys.argv

   try:
      fin = open(argval[1])
   except:
      print('Unable to open',argval[1])
      exit()

   t1 = fin.readline()
   t2 = fin.readline()
   t3 = fin.readline()
   fout = open('hidden.ppm','w')
   fout.write(t1)
   fout.write(t2)
   fout.write(t3)

   final = listcreator(fin)
   update_rgb(final)
   outfile(final,fout)

'''
Pseudocode for List Creator:
Go through the opened file and create a list (mylist) of each line
Create an empty list named final
Go through my list and make a nested list in final of every 3 values
'''
#This function creates a nested list of each pixel's RGB values
#list,file->list
def listcreator(fin):
   mylist = [line.rstrip() for line in fin]
   i = 0
   final = []
   while i < (len(mylist)):
      final.append(mylist[i:i+3])
      i += 3
   return final

'''
Pseudocode for the Update RGB function
Run through each of the pixels
Update the red value for each of the pixels by multiplying it by 10
If the value is over 255, set it to 255
Set the green and blue values as the same value of the red value
Return the updated pixel list
'''
#This function updates the RGB values by multiplying the red value by 10 and matching the green and blue values to the red value
#list->list
def update_rgb(final):
   for val in final:
      val[0] = int(val[0])
      val[0]= val[0]*10
      if val[0] > 255:
         val[0] = 255
      val[1] = val[0]
      val[2] = val[0]
   return final


'''
Pseudocode for Outfile
Run through each of the values of the updated pixel list
Write each value to the specified output file in separate lines
'''
#This function writes each R, G, and B values individually per line to the out file
#list,file->file
def outfile(final,fout):
   for x in final:
         fout.write(str(x[0]) + '\n')
         fout.write(str(x[1]) + '\n')
         fout.write(str(x[2]) + '\n')


if __name__ == '__main__':
   main()

