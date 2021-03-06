import matplotlib.pyplot as plt
import numpy as np

# Points taken from the book-
# Basic idea-
#   - Multiple data points are more accurate than one data point, so don't throw away anything
#   - Always choose a number part way between two data points to get a more accurate estimate
#   - Predict the next measurement and rate of change based on the current estimate
#   - New estimate is then chosen part way between the prediction and next measurement

# 1 epoch -
# Predict step -------------------------------------------> Update Step
#   |_ make estimate based on process model                     |_ take measurement
#   |_ propogates system to next state                          |_ make prediction based on latest measurement



def gh( data, x0, dx, g, h, dt):
    """
    'data' is the data, 'x0' is initial value for state variable
    'x0' is initial value of state variable
    'dx' is initial change rate for state variable
    'g' and 'h' are scale factors
    'dt' is length of time step
    """
    
    est = x0
    filter_result = []

    for z in data:
        # update 
        pred = est + dx * dt
        dx = dx                 #not really required, but helps correlate these two lines with the third basic idea

        #predict        
        residue =  z - pred
        est = pred +  g * residue
        dx = dx + h * residue/dt
        filter_result.append(est)

    return np.array(filter_result)
    

if __name__ ==  "__main__":
    measurements = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
    arr = gh(data = measurements, x0=160., dx=1., g=0.6, h=0.6, dt=1.)

    plt.figure()
    plt.plot(measurements, 'o', label="data")
    plt.plot(arr, 'o--', label="estimates")
    plt.plot(range(160, 172), 'o-', label="weight")
    plt.legend()
    plt.show()


"""
Misc note-

The 'g' factor in this filter basically decides if we want to give more importance to the measurement or
if we want to give more importance to the predictions. So, a high 'g' will make the estimates more closely
resemble the measurements (in this case they are the data provided to us), and a conversely a low 'g' will
make the estimates closely resemble the predictions, which in turn are made based on the process model.

The 'h' parameter affects if we favor the measurement of dx vs our prediction. A larger 'h' causes the system
to respong more rapidly to the changes in the measurements, but it also means that it becomes more susceptable
to noise in the measurements, leading to "less smooth" estimates.

Another important thing to note here is that here we assume that our velocity (or rather, the derivative of
the state variable) is constant, since the prediction is calculated similar t0 x = x + del_x * del_t. So, if
the quantity in the data was "accelerating" (meaning that d2x/dt2 was not 0), then the estimates in this case
("this case" referring to when h and g are constant) will start to lag behind. This lag is called "lag error"
or "systemic error".

Basically, the filter is only as good as the mathematical model of the system (so you better do that very well).

"""
