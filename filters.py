
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
