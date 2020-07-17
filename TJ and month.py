import pandas as pd
import pyodbc

#Gain data from SQL server, tables was imported into SQL Server from two excel file 
#excel file can be found in the same repository
sql_conn = pyodbc.connect('''DRIVER={ODBC Driver 13 for SQL Server};
                            SERVER=ALLENHO\MSSQLSERVER002;
                            DATABASE=TommyJohn;
                            Trusted_Connection=yes''') 
query = '''
select distinct t.Player, t.Position, t.Throws, t.date_of_surgery, p.weight, datediff(day, p.debut, t.date_of_surgery) as daydiff
from TJ$ t
join People$ p
on t.Player=concat(nameFirst,' ',nameLast)
where p.weight is not null and datediff(day, p.debut, t.date_of_surgery)>0 and datediff(day, p.debut, t.date_of_surgery)<7000
order by t.Player;
;
'''
df = pd.read_sql(query, sql_conn)

print(df)

# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# Plot sat variable
sns.distplot(df['daydiff'])
# Display the plot
plt.show()

# Import libraries
import statsmodels.api as sm
from statsmodels.formula.api import glm
import numpy as np
# Fit Poisson regression of sat by width
model = glm('daydiff ~ weight', data = df, family = sm.families.Poisson()).fit()
# Display model results
print(model.summary())

# Compute average weight
mean_weight = np.mean(df['weight'])
# Print the compute mean
print('Average width: ', round(mean_weight, 3))
# Extract coefficients
intercept, slope = model.params
# Compute the estimated mean of y (lambda) at the average width
est_lambda = np.exp(intercept) * np.exp(slope * mean_weight)
# Print estimated mean of y
print('Estimated mean of y at average weight: ', round(est_lambda, 3))

# Compute and print he multiplicative effect
print(np.exp(slope))
# Compute confidence intervals for the coefficients
model_ci = model.conf_int()
# Compute and print the confidence intervals for the multiplicative effect on the mean
print(np.exp(model_ci))

# Plot the data points and linear model fit
sns.regplot('weight', 'daydiff', data = df,
            y_jitter = 0.3,
            fit_reg = True,
            line_kws = {'color':'green', 
                        'label':'LM fit'})
# Print plot
plt.show()

# Add fitted values to the fit_values column of dataframe
df['fit_values'] = model.fittedvalues

# Poisson regression fitted values
sns.scatterplot('weight','fit_values', data = df,
           color = 'red', label = 'Poisson')
# Plot the data points and linear model fit
sns.regplot('weight', 'daydiff', data = df,
            y_jitter = 0.3,
            fit_reg = True,
            line_kws = {'color':'green', 
                        'label':'LM fit'})
# Print plot
plt.show()

