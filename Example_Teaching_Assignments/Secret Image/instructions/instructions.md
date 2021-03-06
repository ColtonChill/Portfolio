# Intermediate Assignment (C++)

In honor of the Olympics, I have created three different methods for distorting an image: bronze, silver, and gold. Your job for this assignment is to create a program that removes the bronze, silver, and gold distortion from an image file.

The images you will be working with will be in PPM Image format, and you will need a little bit of background to understand how this image format works.

## PPM Image Format

The PPM (or Portable Pix Map) image format is encoded in human-readable ASCII text. For those of you who wish to have the experience of reading real documentation, the formal image specification can be found [here](http://netpbm.sourceforge.net/doc/ppm.html).

Sample ppm file:
```
        P3

        4 4

        255

        0  0  0   100 0  0       0  0  0    255   0 255

        0  0  0    0 255 175     0  0  0     0    0  0

        0  0  0    0  0  0       0 15 175    0    0  0

        255 0 255  0  0  0       0  0  0    255  255 255
```

### Image Header

You can think of the image as having two parts, a header and a body. The header consists of four entries:
```
        P3

        4 4

        255
```
P3 is a "*magic number*". It indicates what type of PPM (full color, ASCII encoding) image this is. For this assignment it will always be P3. Next comes the number of columns and the number of rows in the image (4 x 4). Finally, we have the maximum color value 255. This can be any value, but a common value is 255. The way you see the header presented is how it should be spaced out.

### Image Body

The image body contains the actual picture information. Each pixel of the image is a tiny, colored square. The color of each pixel is determined by three integers that represent how much red, green, and blue are present. So, 0 0 0 is the first color of the image, which is black, and the last pixel in the image is 255 255 255, which is white. By varying the levels of the RGB values you can come up with any color in between.

Note that color values must be separated by a space, but after that additional whitespace is ignored by the image viewer. In the sample ppm above we used additional whitespace to format the image so that it is easy for a human to understand, but the computer doesn't care if everything is on one line, if there is one line per line of the image, or some mix.

## Putting it all together

The example image above would look something like this:

![alt text](exampleImage.png)

Keep in mind, each square is one pixel, so the real thing is much smaller (the rendered image was blown up by 5000%).

### How to view PPM files

While PPM files are easy to view as text (you can use Notepad or any other text editor, for instance), and easy to work with in code, they are highly inefficient. Most modern image formats use some kind of compression to make their size reasonable while preserving the image appearance. This is not to say that PPMs don't still have some life in them--one modern use for PPM is an intermediate format when converting images from one type to another.

You will likely need to install a program to view these images on your machine. On Windows machines I find that [Irfanview](https://www.irfanview.com/) is a small download and works quite well. If you are using a Mac or a Linux machine, I would suggest installing [GIMP](https://www.gimp.org/). These programs will also allow you to convert your own images to PPM so you can practice with pictures you took in the past (keep in mind that you may need to make them very small or the resulting PPM will be quite large!).

### Your Assignment

Whew! That may sound like a lot of work, but it's really pretty simple. To make it easy to code I've broken the program into two phases. In the first you are reading in the whole image and writing it to a file without making any changes to the image in the process. Believe it or not, at this point you've written most of the program! In phase II you will add methods that will correct the distortion added to the image.

#### Phase I:

The user will specify the name of the image file. The file will be a text file in PPM format as described in the discussion above.

The user will specify an output filename. The purpose of the program is to make an exact copy of the input file as the output file.

*Hint:* This is not a problem in string processing! Note that many of the functions you will write in Phase II involve doing arithmetic with the pixels so you will want to read them in as integers. You cannot do math with strings!

Your output file can actually be formatted as you like. Whitespace includes newline characters, so you can put them in where you wish. The format allows for it.

Example interaction with the user:
```
        Portable Pixmap (PPM) Image Decoder!

        Enter name of distorted image file: bronzeDistortedImage.ppm

        Enter name of corrected image file: bronzeCorrectedImage.ppm

        bronzeCorrectedImage.ppm created.
```
Your program is NOT responsible for displaying the image in the file, just to manipulate the pixels and create an output file in the proper PPM format.

#### Phase II:

In this phase you will edit your program by writing three different functions to correct the three image distortion types (bronze, silver, and gold):

1. correctBronze – This function takes the RGB values of a pixel and corrects for the bronze distortion method. Images that have been distorted with the bronze method contain the image in the red values, however the red values have all been divided by 10, so they are too small by a factor of 10. The blue and green values are all just meaningless random values ("noise") added to obscure the real image. You must undo these distortions to reveal the real image. First, set all the blue and green values to 0 to get them out of the way. Look at the result. If you look very carefully, you may see the real image, although it is very very dark (way down towards 0). Then multiply each red value by 10, scaling it back up to approximately its proper value.
2. correctSilver – This function takes the RGB values of a pixel and corrects for the silver distortion method. For images that have been distorted using the silver method, the true image is in the blue and green values, however all the blue and green values have been divided by 20, so the values are very small. The red values are all just random numbers, noise added on top to obscure things. Undo these distortions to reveal the true image.
3. correctGold – This method takes the RGB values of a pixel and corrects for the gold distortion method. In gold distorted images the red, green, and blue values have all been stored in the red value. The first three digits contain the red value, the next three digits contain the green value, and the last three digits contain the blue value. The blue and green values are all just meaningless random values ("noise") added to obscure the real image. For example, the following pixel values:
 ```
 155231054    24    235
 ```
Where the distorted red value is 155231054, the distorted green value is 24, and the distorted blue value is 235. Would be corrected to:

```
155     231     54
```
Where the corrected red value is 155, the corrected green value is 231, and the corrected blue value is 54. Undo these distortions to reveal the true image. Hint: use the % and / operators.

__Finally__, you will modify your interaction with the user to accept a distorted image file name, a corrected image file name, and the distortion method that has been applied to the distorted file. Your user interaction might look like the following:
```
        Portable Pixmap (PPM) Image Decoder!

        Enter name of distorted image file: bronzeDistortedImage.ppm

        Enter name of corrected image file: bronzeCorrectedImage.ppm

        Enter the distortion method (b=Bronze, s=Silver, g=Gold):b

        bronzeCorrectedImage.ppm created.
```
     

Your program will read the distorted image file, correct the distortion applied to this file by calling the appropriate function above (correctBronze, correctSilver, correctGold) and write the resulting image to the corrected image file.

I have created three different images, each distorted with a different method for you to test your program with:

bronzeDistortedImage.ppm

silverDistortedImage.ppm

goldDistortedImage.ppm

IMPORTANT: When you download the files above do not open them first (in IrFanView or GIMP or whatever imageviewer you are using) and then save them. If you do this, your imageviewer will most likely try to optimize the file size and modify values it doesn't think are valid. Instead choose to save the file someplace directly. If your browser doesn't give you the option to save (it just opens the file automatically), right-click on the link and click the "Save Link As..." option.

What to turn in: Your `.cpp` file.