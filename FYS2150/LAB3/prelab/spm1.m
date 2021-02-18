A = load('maalinger_deformasjon.dat');
x = A(:,1)
y = A(:,2)


[stigningstall, konstant, error_a] = linaprox(x,y);

tau=[4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
mean(tau);
std(tau)/sqrt(length(tau))
