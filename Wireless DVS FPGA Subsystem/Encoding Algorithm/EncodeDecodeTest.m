close all; clear;
% Requires:
% rleenc.m
% rledec.m
% Images from folder (All 640x640)
%
% Script by: 
% Graeme Fitzpatrick
% University of Strathclyde

%Script will take unencoded test images from the FPGA, encode them and
%save the variables in the workspace, decode them and reconstruct the image.

%%Uncomment which to use, images from table in report of compression rates
%testimage = imread('floatingHead.png'); %%1
%testimage = imread('wave4.png'); %LowNoise 2
%testimage = imread('sideview2.png'); %LowNoise 3
%testimage = imread('wave3.png'); %HighNoise4
testimage = imread('wave1.png'); %LowNoise 5
%testimage = imread('wave2.png'); %HighNoise6
%testimage = imread('Img_test.png'); %%  7
%testimage = imread('sideview.png'); %HighNoise 8

%testimage = imread('3rdpic.png'); %%
%testimage = imread('spooky.png'); %
%testimage = imread('noMovement.png') %Nomovement


%This function can be used to crop 640x640 sections of custom images to test encoder 
%testimage = imcrop(testimage,[1000 1000.5 639 639]);
onedimage = reshape(testimage,[1 size(testimage,1)*size(testimage,2)]);
rlenc = rleenc(onedimage);

%Encoded data in format Ax2 where A(:,2) is encoded data and A(:,1) is
%symbols tied to each element. 
rldec = rledec(rlenc);

rldec(numel(onedimage)) = 0;
reconstruct = reshape(rldec,[640 640]);
figure(1);
imshow(testimage);
figure(2);
imshow(reconstruct);
%Transmission payload minus start bit
payload = rlenc(:,2);

