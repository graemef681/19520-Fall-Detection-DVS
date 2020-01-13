% Andrew Burr - DVS Test - 06/10/19
close all; clear;

videoFileName = 'fall.mp4';
folderName = split(videoFileName, '.');
folderName = string(folderName(1));

command = sprintf('python3 splitIntoFrames.py %s', videoFileName);
[status, commandOut] = system(command);

workingDir = pwd;
cd(folderName);

framesList = dir('*frame*.jpg');

cd(workingDir);

frameArray = [];

for frameNum = 1:numel(framesList)
   frameArray = cat(3,frameArray, rgb2gray(imread(strcat(folderName ,"/", framesList(frameNum).name)))); 
end

differenceArray = [];

for frameNum = 2:numel(framesList)
    differenceframe = frameArray(:,:,frameNum) - frameArray(:,:,frameNum - 1);
    
   
    
    for pixelNum = 1:numel(differenceframe)
        %differenceframe(pixelNum) = log10(double(differenceframe(pixelNum)));
        differenceframe(pixelNum) = double(differenceframe(pixelNum));
    end

    
    average = prctile(differenceframe(:), 97);
    fprintf('Average is %d   \n', average);
    
    for pixelNum = 1:numel(differenceframe)
        if differenceframe(pixelNum) < average
            differenceframe(pixelNum) = 0;
        else
            differenceframe(pixelNum) = 255;
        end
        
    end

    differenceArray = cat(3, differenceArray, differenceframe);
end

% for x = 1:(numel(framesList)-1)
%    figure
%    imshow(differenceArray(:,:,x));
%    pause(0.1);
% end

for x = 1:(numel(framesList)-1)
   imwrite(differenceArray(:,:,x), sprintf('dvs%d.png', x));
end