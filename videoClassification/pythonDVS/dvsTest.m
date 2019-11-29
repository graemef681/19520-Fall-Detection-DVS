% Andrew Burr - DVS Test - 06/10/19
close all; clear;

pythonScriptName = 'test.py'; % change later

% python script to split video into frames
% [status,cmdout] = system(sprintf('python3 %s', pythonScriptName));

if ~(status ==0)
   disp(cmdout);
   error('Python script failed') 
end

framesList = dir('frames\*img*.jpeg');

frameArray = [];

for frameNum = 1:numel(framesList)
   frameArray = cat(3,frameArray, rgb2gray(imread(strcat('frames\', framesList(frameNum).name)))); 
end

differenceArray = [];

for frameNum = 2:numel(framesList)
    differenceframe = frameArray(:,:,frameNum) - frameArray(:,:,frameNum - 1);
    
    for pixelNum = 1:numel(differenceframe)
        differenceframe(pixelNum) = log10(double(differenceframe(pixelNum)));  
    end
    
    average = mean(mean(differenceframe));
    fprintf('Average is %d   \n', average);
    
    for pixelNum = 1:numel(differenceframe)
        if differenceframe(pixelNum) < 6 * average
            differenceframe(pixelNum) = 0;
        else
            differenceframe(pixelNum) = 255;
        end
        
    end

    differenceArray = cat(3, differenceArray, differenceframe);
end

for x = 1:(numel(framesList)-1)
   figure
   imshow(differenceArray(:,:,x));
   pause(0.1);
end