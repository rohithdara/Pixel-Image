#Project 5 Fade
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import sys

argval = sys.argv

'''
Psuedocode for the Main Fade
If the length of the command line argument isn't 5, print the usage statement and exit
Otherwise, try to open the second argument in the command line
If it can't open, print the unable to open message and exit
Try and create the row, column, and radius based on the command line arguments
Open and write the first 3 lines of the input file to the output file
Create a list of all the pixels
Find the width of the image
Fade each of the pixels based on their distance from the specified row and column
Write each of the rgb values of the pixels to the output file on separate lines
'''
def main():
   if len(argval) != 5:
      print('Usage: python3 fade.py <image> <row> <column> <radius>')
      exit()
   try:
      fin = open(argval[1])
   except:
      print('Unable to open',argval[1])
      exit()

   try:
      row = int(argval[2])
      column = int(argval[3])
      radius = int(argval[4])
   except:
      print('Usage: python3 fade.py <image> <row> <column> <radius>')
      exit()


   t1 = fin.readline()
   t2 = fin.readline()
   t3 = fin.readline()
   fout = open('faded.ppm','w')
   fout.write(t1)
   fout.write(t2)
   fout.write(t3)

   final = listcreator(fin)

   pixelmax = t2.split()
   colmax = int(pixelmax[0])
   rowmax = int(pixelmax[1])

   fade_image(final,colmax,row,column,radius)
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
Pseudocode for the Fading
Run through each pixel of the ppm file
Calculate the distance from each point to the specified row and column
Create a fade value per pixel
If the fade value is less than 0.2, set it equal to 0.2
Multiply each of the rgb values in the pixel by the fade value
Return the updated pixel list
'''

#This function updates the pixel list by multiplying by a number based on the pixel's distance from the specified point and the specified radius
#list,int,int,int,int->list
def fade_image(final, colmax, row, column, radius): 
   for pixel in range(len(final)):
      rowz = pixel // colmax
      colz = pixel % colmax
      distance = ((row-rowz)**2 + (column-colz)**2)**0.5
      fadeval = (radius - distance) / radius
      if fadeval < 0.2:
         fadeval = 0.2  
      final[pixel][0] = int(int(final[pixel][0]) * fadeval)
      final[pixel][1] = int(int(final[pixel][1]) * fadeval)
      final[pixel][2] = int(int(final[pixel][2]) * fadeval)
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
