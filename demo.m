% Example of Situation corresponding to a paper being prepared for Sensors
%
% We have: models of IMU reconstructions: zhu, pep, young
% For some of these models we have versions
% Young has versions: 'pure complementary', 'perfect complementary'
% Peppoloni has versions: 'original','svd','reorder'
% Then the version reorder has three variants: 1,2,3
%
% In addition to models we have cases of datasets: aug10 and sim

% First we build the structure
s = [];
s.name = 'model';
s.values = {'zhu','pep','young'};
s.children = [];

v = [];
v.name = 'version';
v.values = {'pure complementary', 'perfect complementary'};
s.children.young = [v];

v = [];
v.name = 'version';
v.values = {'original','svd','reorder'};

q = [];
q.name = 'order';
q.values = [1,2,3];
v.children.reorder = [q];
s.children.pep = [v];

c = [];
c.name = 'case';
c.values = {'aug10','sim'};
c.children = [];

% we obtain all the combinations (Y) as indices
% togheter with adjusted and ordered specs (ys)
[Y,ys] = gentestcases([c,s]);

% we can then convert them to cell array with strings and a sequence of
% names that ease lookup
[Yc,yn] = cases2values(Y,ys);

Y
ys.fullname
yn
assert(isfield(yn,'model_pep__version_reorder__order'))
assert(length(ys) == size(Y,1)) %  in any case
assert(size(Y,1) == 5) % for this situation
assert(size(Y,2) == 16) % for this situation
