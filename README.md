# image-compression-python
In a straightforward 24-bit color representation of an image, each pixel is 
represented as three 8-bit unsigned integers (ranging from 0 to 255) that specify
the red, green and blue intensity values. This encoding is often refered to as
the RGB encoding. Our image contains thousands of colors, and in this project
we reduce the number of colors to 16 colors.

By making this reduction, it is possible to represent (compress) the photo
in an efficient way. Specifically, we only need to store the RGB values of
the 16 selected colors, and for each pixel in the image we now need to only
store the index of the color at that location (where only 4 bits are necessary
to represent 16 possibilities). We use K-means algorithm to select the 16 colors 
that will be used to represent the compressed image.
