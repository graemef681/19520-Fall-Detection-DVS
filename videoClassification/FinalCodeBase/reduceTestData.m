close all; clear;

frameList = dir('*.png');
frameNames = strings(numel(frameList), 1);


for x = 1 : numel(frameList)
    frameNames(x) = frameList(x).name;
end

msize = numel(frameList);
idx = randperm(msize);
frameNamesRandom = frameNames(idx(1:x));

for y = 607 : numel(frameList)
    delete(frameNamesRandom(y));
end