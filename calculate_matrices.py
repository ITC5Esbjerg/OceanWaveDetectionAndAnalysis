import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



class CalculateMatrices:
    
    def __init__(self, generalFilePath, numberOfArrays):
        self.generalFilePath = generalFilePath
        self.frames = []
        self.anim_images = []
        self.fig, self.ax = plt.subplots()
        self.loadArrays(numberOfArrays)
        self.convertAnimationToMatrix()
    
    #Load all the matrices containing X, Y and height of the waves
    def loadArrays(self, numberOfArrays):
        for i in range(numberOfArrays):
            specificFilePath = self.generalFilePath.format(i)
            arrayData = np.load(specificFilePath)
            self.frames.append(arrayData)
    
    #Create an animated image of each matrix with X, Y and height of the waves
    def animateArrays(self, i):
        self.ax.clear()
        self.contour = self.ax.contourf(self.frames[i], levels=50, cmap='coolwarm')
        return self.contour
    
    #Display a particular frame just to see how it looks (testing purpose)
    def displaySingleFrame(self, frame_index):
        self.ax.clear()
        self.animateArrays(frame_index)
        plt.show()
    
    #Animate each starting matrix and then convert it into a numpy array with different pixels values    
    def convertAnimationToMatrix(self):
        color_matrices = []

        #Ensure the use of the 'Agg' backend, which is for PNGs
        plt.switch_backend('Agg')
        
        #Create an animated image for each given matrix
        for frameMatrix in self.frames:
            self.ax.clear()
            contour = self.ax.contourf(frameMatrix, levels=50, cmap='coolwarm')
            self.fig.canvas.draw()

            #Convert the image buffer to a numpy array
            image = np.frombuffer(self.fig.canvas.tostring_rgb(), dtype=np.uint8)
            width, height = self.fig.canvas.get_width_height()
            image = image.reshape((height, width, 3))

            color_matrices.append(image)

        self.anim_images = color_matrices


arraysPath = "/Users/dawid/Documents/Coding/Visual Studio/Project 2023_2024/Wave plots/array_{}.npy" #Actual path where the arrays from the camera are stored
number_of_arrays = 20   #Number of .npy files (arrays)

calcMatrices = CalculateMatrices(arraysPath, number_of_arrays)
color_matrices = calcMatrices.anim_images   #a list of already converted animated images to RGB pixels values





