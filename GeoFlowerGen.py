import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Function to generate points on a rose curve
def rose_curve(theta, A, k):
    return A * np.cos(k * theta)

def PlotFunc(out_name:str="name.png",a:int=1,k:int=6):
    # Set the parameters
    A = a  # amplitude
    k = k  # number of petals

    # Generate a sequence of theta values
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Calculate corresponding points on the rose curve
    r = rose_curve(theta, A, k)

    # Convert polar coordinates to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the rose curve without any axes or labels
    plt.plot(x, y, color='red')
    plt.axis('off')  # Turn off the axes
    plt.savefig(out_name)
    #plt.show()

    # Open the saved image using PIL
    image = Image.open(out_name)

    # Convert the image to RGBA (add an alpha channel)
    image = image.convert('RGBA')

    # Get the image data as a NumPy array
    image_data = np.array(image)

    # Set white pixels to be transparent
    white_pixels = (image_data[:, :, :3] != [0, 0, 0]).all(axis=2)
    image_data[white_pixels] = [0, 0, 0, 0]

    # Create a new image with the modified data
    new_image = Image.fromarray(image_data)
    ##gpt do here clean the plt!
    new_image.save(out_name)
    plt.clf()

    # Save the final image with transparency

# Show the final image
#new_image.show()

if __name__=="__main__":
    i=20
    for j in range(30):
        Name="out\\asset"
        endian=str(i)+"_"+str(j)+".png"
        outN=Name+endian
        if  i!=j and j>1 and i>1:
           PlotFunc(outN,i,j)