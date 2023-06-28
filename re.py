import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

def reliability_analysis():
    # Constants
    beta_T = 2.33
    num_simulations = 50000

    # Soil properties
    phi_mean = 36
    phi_cov = 0.06
    c_mean = 5
    c_cov = 0.30
    gamma_mean = 21
    gamma_cov = 0.05

    # Nail properties
    lamda_r_mean = 1
    lamda_r_cov = 0.298
    lamda_q_mean = 0.95
    lamda_q_cov = 0.382
    H = 10
    qs = 12
    i = 15
    h = 0.5
    DD = 0.15
    L = 4
    Sh = 1  # Assuming a value of 1 for horizontal soil nail spacing
    Sv = 1  # Assuming a value of 1 for vertical soil nail spacing

    # Function to calculate qu
    def gepModelqu(d):
        G1C2 = -3.48844627213141
        G1C5 = -6.20175817133091
        G2C6 = 5.49893271745485
        G2C5 = -4.29113855828654
        G2C9 = -3.95507070751173
        G2C2 = 3.49594053665271
        G3C0 = -7.14015242255928
        G3C7 = -9.77987402445779
        G4C2 = 7.15933713797418
        G4C8 = -6.18209711691404
        G4C9 = 4.90646790649796
        G4C7 = 3.12698433622949
        G4C0 = -5.74391414499274

        L = 0
        DD = 1
        i = 2
        sigma_v = 3
        c = 4
        phi = 5

        y = 0.0

        y = ((d[L] + (((d[phi] - d[i]) + (d[sigma_v] + d[phi])) / 2.0)) + (G1C2 / (((d[phi] / d[L]) + G1C5) / 2.0)))
        y = y + ((G2C6 * ((G2C9 - G2C6) + (G2C2 / d[DD]))) + (((d[phi] + d[phi]) - d[i]) - (G2C5 * d[c])))
        y = y + ((((d[L] / d[DD]) - (G3C0 * d[L])) - d[phi]) / (
                    ((((G3C7 + G3C7) + d[phi]) / 2.0) + (d[i] - d[phi])) / 2.0))
        y = y + (((((G4C7 * G4C7) / ((d[c] + G4C0) / 2.0)) + ((d[L] - d[DD]) * d[i])) / 2.0) - (
                    (G4C8 + d[c]) / 2.0))
        y = y + ((G4C9 * d[i]) / 2.0)

        return y

    # Calculate nail pullout resistance (Pult)
    def calculate_Pult(D, L, qu):
        return 3.14 * D * L * qu

    # Calculate nail tensile load (Tn)
    def calculate_Tn(H, h, Ka, gamma, qs, Sh, Sv):
        return h * Ka * (gamma * H + qs) * Sh * Sv

    # Generate random samples for the uncertain variables
    phi_samples = lognorm.rvs(s=phi_cov, scale=phi_mean, size=num_simulations)
    c_samples = lognorm.rvs(s=c_cov, scale=c_mean, size=num_simulations)
    gamma_samples = lognorm.rvs(s=gamma_cov, scale=gamma_mean, size=num_simulations)
    lamda_r_samples = np.random.normal(loc=lamda_r_mean, scale=lamda_r_mean * lamda_r_cov, size=num_simulations)
    lamda_q_samples = np.random.normal(loc=lamda_q_mean, scale=lamda_q_mean * lamda_q_cov, size=num_simulations)

    # Perform reliability analysis
    Pult_samples = []
    for i in range(num_simulations):
        phi = phi_samples[i]
        c = c_samples[i]
        gamma = gamma_samples[i]
        lamda_r = lamda_r_samples[i]
        lamda_q = lamda_q_samples[i]

        qu = gepModelqu([L, DD, i, phi, c, phi])
        Pult = calculate_Pult(DD, L, qu)
        Tn = calculate_Tn(H, h, 0.0, gamma, qs, Sh, Sv)

        g = lamda_r * Pult - lamda_q * Tn

        if g >= 0:
            Pult_samples.append(lamda_r * qu)

    # Apply model bias correction
    Pult_samples = np.array(Pult_samples) * beta_T

    # Plot histogram
    plt.hist(Pult_samples, bins=50, edgecolor='black', alpha=0.7)
    plt.xlabel('Nail Bond Strength (lamda_r x qu) - Corrected')
    plt.ylabel('Frequency')
    plt.title('Histogram of Predicted Nail Bond Strength')
    plt.grid(True)
    plt.show()


# Run the reliability analysis and plot the histogram
reliability_analysis()
