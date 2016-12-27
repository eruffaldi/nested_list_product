%
% Given [Y,ys] produced by gentestcases we convert them to cell array
% and then to list of names in a structure
% 
% Emanuele Ruffaldi 2016
function [Yv,yn] = cases2values(Y,ys)

yn = [];
Yv = cell(size(Y));
for I=1:length(ys)
    yn.(ys(I).fullname) = I;
    q = Y(I,:) ~= 0;
    if iscell(ys(I).values)
        Yv(I,q) = ys(I).values(Y(I,q));
    else
        Yv(I,q) = num2cell(ys(I).values(Y(I,q)));
    end
end
