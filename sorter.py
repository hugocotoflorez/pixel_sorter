from PIL import Image
import colorsys


with Image.open('image.jpg') as im:
    width, height = im.size
    pixels = list(im.getdata())

    keys = {
        'l':lambda px: 0.299*px[0] + 0.587*px[1] + 0.114*px[2] ,# luminosidad
        'h':lambda px:(colorsys.rgb_to_hsv(*px)[0]) , #hue
        's':lambda px:(colorsys.rgb_to_hsv(*px)[1]),#spectre
        'v':lambda px:(colorsys.rgb_to_hsv(*px)[2])#vibrance
    }
    
    #SORT: 
    
    #all
    pixels.sort(key=keys['v'])
    
    #each column
    for h in range(width):
        pixels[h::width] = sorted(pixels[h::width],key=keys['h'])                       
       
    #each line
    for h in range(height):
        pixels[h*width:h*width+width] = sorted(pixels[h*width:h*width+width],key=keys['l'])
              
        
                                            
   
    im.putdata(pixels)     
    im.show()

    


    
