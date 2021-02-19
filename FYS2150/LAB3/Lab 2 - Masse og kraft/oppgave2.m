T = 1/15 * [6.9 6.39 6.75]

mean(T)

se = std(T)/sqrt(length(T))

e_tot = sqrt(se^2 + (1/100)^2)