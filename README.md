# Sudoku-Solver
I tried to understand and implement a sudoku solver with the help of code written and explained by @Aakash Jawar. Link: https://medium.com/@aakashjhawar/sudoku-solver-using-opencv-and-dl-part-1-490f08701179
## Procedure:
The Procedure involves three main parts. 
*  Preprocess the Image
*  Extract the puzzle
*  Solve and Display
### Preprocessing the image:
The image is performed with Gaussian blur and Adaptive Thresholding. Now the resultant binary image is fed into a dilation unit for better results in later events.
The contours are detected and the contour with largest area is expected to be the puzzle's boundary. Now skewing is applied in case of distorted image. After this, the puzzle boundary coordinates are used to find the length of each of the 81 identical cells in the puzzle. They are all cropped and added to a list in row by row fashion.
<img src = "Images/First cell cropped cell.png" width=200>
<img src = "Images/Another cell.png" width=200>
<img src = "Images/Empty cell.png" width=200>
