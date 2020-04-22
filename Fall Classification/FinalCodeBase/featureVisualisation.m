close all; clear;


load('netTransfer-smallNetV4.mat');


net = netTransfer;
net.Layers
layer = 2;
name = net.Layers(layer).Name;

channels = 1:8;

I = deepDreamImage(net,layer,channels,'PyramidLevels',5);
%I = deepDreamImage(net,layer,channels);

figure
I = imtile(I,'ThumbnailSize',[128 128]);
imshow(rgb2gray(I))
title(['Layer ',name,' Features'])

% I = deepDreamImage(net,layer,channels, 'Verbose',false, 'NumIterations',50);
% 
% figure
% I = imtile(I,'ThumbnailSize',[128 128]);
% imshow(I)
% name = net.Layers(layer).Name;
% title(['Layer ',name,' Features'])
