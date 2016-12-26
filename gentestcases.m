%
% [Y,ys] =  gentestcases(specs)
% [Y,ys,yn] =  gentestcases(specs)
%
% Input: specs as array of structure. Each structure is:
%   .name = name of the enumeration
%   .values = cell array of strings, or array of values
%   .children = structure in which a field
%
% For numeric values the children has to be expressed in textual form as
% "v%d_%d", e.g. value of 10.2 becomes v10_2
%
% Output: Y is a matrix of indices [M,N] with NaN where indices are not
% applicable. Each row correspond to a possible enumeration spec, whil N
% are the overall cases
%
% Output: ys is an array of structures flattened, one for every row of Y
% matrix. Similar to the specs in input, but it adds a fullname field
%
% Optional Output: yn is a structure with full names of terms that can be
% used to lookup into Y or into ys.
%
% Use cases2values for generating effective values as cell array
%
% Emanuele Ruffaldi 2016
function [Y,ys,yn] =  gentestcases(specs)

assert(isstruct(specs));

% build sizes
alls = cell(length(specs),1);
ys = [];
for I=1:length(specs)
    s = specs(I);
    s.fullname = s.name;
    alls{I} = 1:length(s.values);
    if isfield(s,'children') == 0
        s.children = [];
    end
    ys = [ys;  s];
end


Y = combvec(alls{:});

for I=1:length(specs)
    s = specs(I);
    if isfield(s,'children') && isempty(s.children) == 0
        ff = fieldnames(s.children);
        for K=1:length(ff)
            [J,v] = locatevalue(ff{K},s.values); % index of children K inside value check for nubers
            if isempty(J)
                continue;
            end
            [Yc,ysc] = gentestcases(s.children.(ff{K}));
            % Yc has rows as the domain of the entity and its descendents
            % Yc has cols as the variants
            
            % enlarge the domain (rows) to accomodate all the Yc            
            prefix = [s.name '_' v];
            k = size(Y,1);
            for Q=1:length(ysc)
                fn = [prefix '__' ysc(Q).fullname];
                ysc(Q).fullname = fn;
            end
            ys = [ys; ysc]; 
                
            % enlarge ths spaces by replicating the cols containing the key           
            sK = Y(I,:) == J;
            YK = combvec(Y(:,sK),Yc);
            
            YnK = Y(:,sK == 0);
            YnK = [YnK ; nan(size(Yc,1),size(YnK,2))]; % not specific 
            
            % YnotK  ,  YK repeated
            % nan    ,  YC
            Y = [YnK,YK]; % rebuild            
        end
    end
end

if nargout == 3
    % used only for external interface
    yn = [];
    for I=1:length(ys)
        yn.(ys(I).fullname) = I;
    end
end


function [J,v] = locatevalue(name,values)

if iscell(values)
    if ischar(values{1})
        J = find(strcmp(values,name),1,'first');
        if isempty(J)
            v = [];
        else
            v = values{J};  
        end
    else
        error('unsupported content in cell');
    end
else
    % extract value from name: vint_dot
    v = name(2:end);
    name = name(2:end);
    name(name == '_') = '.';
    value = eval(name);
    J = find(values == value,1,'first');
end
    

