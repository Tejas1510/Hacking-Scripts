## Gradient Descent in Python

### What is gradient descent ?
``` It is an optimization algorithm to find the minimum of a function. We start with a random point on the function and move in the negative direction of the gradient of the function to reach the local/global minima.```

![endpoint](https://github.com/Tejas1510/hacking-tools-scripts/blob/main/Python/GradientDescent/images/image1.jpeg)

### Introduction
``` 
Gradient descent is an optimization algorithm that is used to find the local minima of a differentiable function.

In the realm of Machine Learning, It is used to find the values of parameters of a differentiable function such that the loss is minimized.

Let us understand the gradient descent algorithm with a simple practical example.
Imagine a blind hiker is trying to get down a hill to its lowest point as shown in the image above.
There is no way for the hiker to see which direction to go as he is blind. However, there is one thing hiker understands clearly If he is going down, its the right progress and if he is going up, it is wrong progress.
Therefore, if he keeps taking small steps, that takes him downwards, he will be able to get down the lowest point on the hill.
Here, taking small steps can be considered as a learning rate, and the height above the lowest point can be considered as the loss.
Also reaching the lowest point of the hill can be considered as a convergence
which indicates no further possibility of going down, and the loss is minimum 
```



### Code

### Step 1: Initialize parameters
```cur_x = 3 # The algorithm starts at x=3
rate = 0.01 # Learning rate
precision = 0.000001 #This tells us when to stop the algorithm
previous_step_size = 1 #
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter
df = lambda x: 2*(x+5) #Gradient of our function 
```
### Step 2: Run a loop to perform gradient descent :
```while previous_step_size > precision and iters < max_iters:
    prev_x = cur_x #Store current x value in prev_x
    cur_x = cur_x - rate * df(prev_x) #Grad descent
    previous_step_size = abs(cur_x - prev_x) #Change in x
    iters = iters+1 #iteration count
    print("Iteration",iters,"\nX value is",cur_x) #Print iterations
    
print("The local minimum occurs at", cur_x)
```
### Output
```From the output below, we can observe the x values for the first 10 iterations- which can be cross checked with our calculation above. The algorithm runs for 595 iterations before it terminates.```

![endpoint](https://github.com/Tejas1510/hacking-tools-scripts/blob/main/Python/GradientDescent/images/image2.png)

![endpoint](https://github.com/Tejas1510/hacking-tools-scripts/blob/main/Python/GradientDescent/images/image3.png)

![built with love](https://forthebadge.com/images/badges/built-with-love.svg)

Check out my Github profile [Tejas1510!](https://github.com/Tejas1510)
