from PIL import Image

# Convert student number to binary
number = 3722243
numberBinary = format(number, "b")
print(numberBinary)

# Generate list of selected pixels
pixels = []
for i in range(1,23):
    pixels.append((i*10,i*50))

# Open image
image = Image.open("mona_lisa.jpg")
newImage = image.copy()

for i in range (0,22):
    pixel = newImage.getpixel(pixels[i])
    red = format(pixel[0],"b")
    newRed = (int(red) & ~1) | int(numberBinary[i])
    newPixel = (int(str(newRed),2),pixel[1],pixel[2])
    newImage.putpixel(pixels[i],newPixel)
    print("Selected binary character in student number: " + str(numberBinary[i]))
    print("Selected pixel value: " + str(pixel))
    print("Selected pixel's red value (binary): " + str(red))
    print("Selected pixel's new red value (binary): " + str(newRed))
    print("Selected pixel's new value: " + str(newPixel))
    print("---")

newImage.save("stego_mona_lisa.jpg")