import numpy as np
import matplotlib.pyplot as plt # This displays graphs once they have been created

############
def graph_df (x_rolls, y, n):
    np.random.seed(0)
    rand  = np.random.randint(len(x_rolls[0]), size= n) ## @@@@ RED FLAG: random sampling here destroys the order -> ask Prof
    
    for x in x_rolls:
        plt.figure(figsize=(6, 4))
        S_Flag = True
        B_Flag = True

        for t in range (n):
            i = rand[t]
            lineSpec =  np.array(x.iloc[i]).flatten()

            if y[i] == 'S':
                if S_Flag:
                    plt.plot(np.array(x.columns), lineSpec, color = 'red', label = "S") # plotting the good apples
                    S_Flag = False
                plt.plot(np.array(x.columns), lineSpec, color = 'red') # plotting the good apples
            if y[i] == 'B':
                if B_Flag == True:
                    plt.plot(np.array(x.columns), lineSpec, color = 'blue', label = "B") # plotting the good apples
                    B_Flag = False
                plt.plot(np.array(x.columns), lineSpec, color = 'blue') # plotting the bad apples

        plt.title("GS apples", fontweight ='bold', fontsize =12)    
        plt.xlabel("Wavelength", fontweight ='bold', fontsize =12)
        plt.ylabel("Frequency", fontweight ='bold', fontsize =12)
        # plt.ylim([-.3,2.2])

        plt.legend()

        plt.show()