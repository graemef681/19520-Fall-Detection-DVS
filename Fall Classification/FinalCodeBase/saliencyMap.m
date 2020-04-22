close all; clear;


load('netTransfer-smallNetV4.mat');

net = netTransfer;

im = imread('newDataset/fall/fall3.mp4-dvs11.png');
figure, set(gcf, 'color', 'w');
imshow(im);

act1 = activations(net,im,'fc');


figure, set(gcf, 'color', 'w');
%I = imtile(mat2gray(act1),'GridSize',[4 8]);
I = imtile(act1,'GridSize',[4 8]);
imshow(I)
