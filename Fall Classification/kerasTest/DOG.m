close all;

I = imread('testImage.png');
I = rgb2gray(I);
figure, imshow(I)

k = 50;
sigma1 =  0.1;
sigma2 = sigma1*k;

hsize = [11,11];

h1 = fspecial('gaussian', hsize, sigma1);
h2 = fspecial('gaussian', hsize, sigma2);

gauss1 = imfilter(I,h1,'replicate');
gauss2 = imfilter(I,h2,'replicate');

dogImg = gauss1 - gauss2;

dogMean = mean(dogImg);

figure;
subplot(1,2,1);
imshow(dogImg);
title('Pre threshold');

for x = 1:numel(dogImg)
   if dogImg(x) > dogMean * 5
      dogImg(x) = 255;
   else
      dogImg(x) = 0;
   end
end

subplot(1,2,2);
imshow(dogImg);
title('Post threshold');