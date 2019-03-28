#Project 5 Blur
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01


import sys

argval = sys.argv
print(argval)

'''
Pseudocode for Blur Main
Check the length of the command line argument
If the length isn't 3 or 4, print the usage statement and exit
Otherwise, try to open the first argument in the command line 
If it isn't an openable ppm file, print that it was unable to open and exit
If the length of the argument was 3, set the blurfactor equal to the 3rd argument in the command line
If the length of the argument was 2, default the blurfactor to 4
Open and read the first 3 lines of the ppm file ad write it to the output file after opening the output file
Create the list of the pixels
Find the width of the ppm file
Blur each of the pixels based on their neighboring values
Write each pixel to the output file
'''
#This function runs the blur function
#->
def main():
   if len(argval) != 3 and len(argval) !=2:
      print('Usage: python3 blur.py <image> <OPTIONAL:reach>')
      exit()
   try:
      fin = open(argval[1])
   except:
      print('Unable to open',argval[1])
      exit()

   if len(argval) == 3:
      try:
         blurfactor = int(argval[2])
      except:
         print('Usage: python3 blur.py <image> <OPTIONAL:reach>')
         exit()
   if len(argval) == 2:
      blurfactor = 4


   t1 = fin.readline()
   t2 = fin.readline()
   t3 = fin.readline()
   fout = open('blurred.ppm','w')
   fout.write(t1)
   fout.write(t2)
   fout.write(t3)

   final = listcreator(fin)

   pixelmax = t2.split()
   colmax = int(pixelmax[0])
   rowmax = int(pixelmax[1])

   final2 = blurring(final,colmax,blurfactor)
   outfile(final2,fout)

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
Pseudo Code for Blurring:
Create an empty list named final2
Use a for loop to run through each pixel in the image
Create aother empty list
Find the start of the row by subtracting the reach (it also makes sure that the value is above 0)
Find the end of the row by adding the reach (it also makes sure the value doesn't surpass the picture length)
Find the start of the column by subtracting the reach (it also makes sure that the value is above 0)
Find the end of the column by adding the reach (it also makes sure the value doesn't surpass the picture length)
Create 3 empty lists for each of the rgb values
Run through each row of each column
Convert the 2D list into a 1D list
Add each rgb value to their specified list
Find the average of each rgb list
Add the average of each list to the final 2 list
Convert the 2D list into a 1D list
'''
#This function updates the pixel list by averaging each rgb value based on the values around it(range depends on specified reach)
#list,int,int->list
def blurring(final,colmax,blurfactor):
   final2 = []
   for pixel in range(len(final)):
      temp = []

      row_s = max((pixel // colmax) - blurfactor, 0) 
      row_e = min((pixel // colmax) + blurfactor, (len(final) - 1) // colmax)  
      col_s = max((pixel % colmax) - blurfactor, 0)  
      col_e = min((pixel % colmax) + blurfactor, (len(final) - 1) % colmax)

      red = []
      green = []
      blue = []
      for x in range(col_s,col_e+1):
         for y in range(row_s,row_e+1):
            update_pixel = y * colmax + x
            red.append(int(final[update_pixel][0]))
            green.append(int(final[update_pixel][1]))
            blue.append(int(final[update_pixel][2]))

      temp.append(sum(red)//len(red))
      temp.append(sum(green)//len(green))
      temp.append(sum(blue)//len(blue))
      final2.append(temp)
   return final2

'''
Pseudocode for Outfile
Run through each of the values of the updated pixel list
Write each value to the specified output file in separate lines
'''
#This function writes each R, G, and B values individually per line to the out file
#list,file->file
def outfile(final2,fout):
   for x in final2:
         fout.write(str(x[0]) + '\n')
         fout.write(str(x[1]) + '\n')
         fout.write(str(x[2]) + '\n')


if __name__ == '__main__':
   main()
