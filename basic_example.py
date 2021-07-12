import matplotlib.pyplot as plt

weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 169.6, 167.4, 166.4, 171.0, 171.2, 172.6]

time_step = 1.0
weight_scale = 4.0/10
gain_scale = 1./3

def predict_gh(estimated_weight, initial_gain_rate, do_print=False):

    estimates, predictions = [estimated_weight], []

    gain_rate = initial_gain_rate

    # the book says that it is convention to use z for measurements
    for z in weights:
        predicted_weight = estimated_weight + gain_rate * time_step     # make prediction

        residue = z - predicted_weight                                  # diff b/w measurement and prediction
        estimated_weight = predicted_weight + weight_scale * residue    # calc estimate
        gain_rate = gain_rate + gain_scale * (residue)/time_step        # update the gain
        
        estimates.append(estimated_weight)
        predictions.append(predicted_weight)
        if do_print:
            print(estimated_weight, predicted_weight, sep=', ')

    return estimates, predictions

if __name__ ==  "__main__":
    initial_estimate = 160.
    estimates, predictions = predict_gh(initial_estimate, -1, True)

    plt.figure()
    plt.plot(estimates, label="e")
    plt.plot(predictions, label="p")
    plt.plot(weights, label="w")
    plt.plot(range(160, 172), label="line")
    plt.legend()
    plt.show()
