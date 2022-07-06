function [Z] = f_eulerd2(dx,dy,F0,I,h)

    Z = [F0];
    z1 = F0;

    xi = I(1);
    xf = I(2);

    x0 = F0(1);
    y0 = F0(2);

    n = (xf-xi)/h;
        for k = 1:n
            y0 = y0+h*dy(x0,y0);
            x0 = x0+h*dx(x0,y0);
            z1 = [x0;y0];
            Z = horzcat(Z,z1);
        end
end