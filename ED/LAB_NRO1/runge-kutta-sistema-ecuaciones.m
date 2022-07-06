function [x,y] = f_runge_kutta(func,intervalo,y0,h)

    colors = ['b','r','g','c','m','y','k','b','r','g','c','m','y','k'];
    x0 = intervalo(1);
    xf = intervalo(2);
    
    x = [x0];
    y = [y0];
    
    xtemp = x0;
    ytemp = y0;
    
    n = (xf-x0)/h;
    
    for i=1:n
        k1temp = func(ytemp,xtemp);
        k2temp = func(ytemp+(1/2)*h*k1temp,xtemp+(1/2)*h);
        k3temp = func(ytemp+(1/2)*h*k2temp,xtemp+(1/2)*h);
        k4temp = func(ytemp+h*k3temp,xtemp+h);

        ytemp = ytemp + h*(1/6)*(k1temp+2*k2temp+2*k3temp+k4temp);
        xtemp = xtemp+h;
        
        x = horzcat(x,xtemp);
        y = horzcat(y,ytemp);
    end
    
end