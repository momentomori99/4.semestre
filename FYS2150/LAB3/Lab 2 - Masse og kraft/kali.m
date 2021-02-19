masse = [10, 100, 500, 1000, 1500, 2000]
lengde = [0.1, 0.6, 3.0, 5.9, 8.7, 11.4]

[a, b, error_a, error_b] = linaprox(masse,lengde)

% plot(masse, lengde, 'r--o', masse, 0.0913 +0.0057*masse, 'b' )
% legend('målte verdier', 'linær tilnærming, 0.0913 + 0.0913x = y')
% xlabel('masse')
% ylabel('lengde')
% grid on

% l_al = [12.4 12.3 12.3]
% avg_l= mean(l_al)
% 
sys_error = 0.001
% 
% error_l_al = sqrt(std(lengde_al)/length(lengde_al) 

l = 12.3;

%l = am + b

m = (l-b)/a

