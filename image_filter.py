# Image-Filter

#image_playground.py
import filters
import image_io

height = 256
width = 20 
image = []
for i in range(height):
    row = []
    for col in row:
        col = [255, 255, 255]
        row.append(col)
        image.append(row)
        
image_io.write_to_file("output/image.png", image)

#filters.py
#Turns a given picture grey

def grayscale(image_matrix):
  for pixels in image_matrix:
    for pixel in pixels:
      R = pixel[0]
      G = pixel[1]
      B = pixel[2]
      
      avg = (R + G + B)//3

      pixel[0] = avg
      pixel[1] = avg
      pixel[2] = avg 
      
  return image_matrix
