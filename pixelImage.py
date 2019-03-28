#Project 5 Pixel Image
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import sys

argval = sys.argv

'''
Pseudocode for the main Pixel Image function
Based on the # of arguments in the command line, the function will run either the fade, blur, or puzzle function
If the # of arguments is 5, run through the conditions for the fade function and run the fade function
If the # of arguments is 3, run through the conditions for the blur function and run the blur function
If # of arguments is 2, run through the conditions for the puzzle function and run the puzzle function
If it is not 5, 3, or 2 print the usage statement and exit the function
The pseudocode for the conditions and the functions can be found in each of the separate python files
'''
#This function runs either the fade,blur,or puzzle functions based on the command line argument
#->
def main():

   if len(argval) == 5:
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
         print('Usage: python3 pixelImage.py <image> <row> <column> <radius>')
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

   if len(argval) == 3:
      try:
         fin = open(argval[1])
      except:
         print('Unable to open',argval[1])
         exit()

      try:
         blurfactor = int(argval[2])
      except:
         print('Usage: python3 pixelImage.py blur <image> <reach>')
         exit()
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

   if len(argval) == 2:
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

   elif len(argval) != 5 and len(argval) != 3 and len(argval) !=2:
      print('Usage: python3 pixelImage.py <parameters for needed function>')

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


