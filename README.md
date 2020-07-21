Try to find out how MLB players' weight affect the time between their debut and Tommy John surgery date

Gather data from Lahman's baseball database's 'People' table and list of players who underwent Tommy John surgery from Wikipedia

Using SQL Server to prepare the data

Using Python(Spyder) to perform poisson regression, for the data linear regression is actually better. But chose poisson for self-training and diversity


Result:
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      8.6950      0.016    528.132      0.000       8.663       8.727
weight        -0.0059    7.8e-05    -75.072      0.000      -0.006      -0.006

Average weight:  212.665

Estimated mean of y at average weight:  1720.251

With one unit increase of weight, the mean response of the time between their debut and Tommy John surgery date will multiply by 0.9941637034397474, which imply 0.6% decrease.



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
One sentence conclusion: it really didn't matter much for the weight of players on the time between their debut and Tommy John surgery date, but we can slightly imply they are negatively correlated. 
