function [a,b,error_a,error_b] = linaprox(x,y)
%Kalle eksempel: [stigningstall, konstant, error_a] = linaprox(x,y)
%Denne bruker for å tilnærme linær funksjon for gitte punkter i array-form
%_:)
    n = length(x);
    
    xy_ = 0;
    x_ = 0;
    y_ = 0;
    x2_ = 0;
    y2_ = 0;
    
    for i = 1:n
        xy_ = xy_ + x(i)*y(i);
        x_ = x_ + x(i);
        y_ = y_ + y(i);
        x2_ = x2_ + x(i)^2;
        y2_ = y2_ + y(i)^2;
        
        
        
    end
    E = xy_ - 1/n*x_*y_;
    D = x2_ - 1/n*x_^2;
    F = y2_ - 1/n*y_^2;
    y_strek = 1/n*y_;
    x_strek = 1/n*x_;
    
    a = E/D;
    b = y_strek - a*x_strek;
    error_a = sqrt((1/(n-2))*(D*F - E^2)/D^2);
    
    error_b = sqrt((1/(n-2))*((D/n) + mean(x)^2)*((D*F - E^2)/D^2));
   
    
    
end