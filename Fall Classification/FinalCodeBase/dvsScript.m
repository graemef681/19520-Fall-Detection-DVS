NUMBER_OF_CLIPS = 16;
CLIP_NAME = "walk";

homeDir = pwd;

for x = 1:NUMBER_OF_CLIPS
    disp(strcat("File number: ", string(x)));
    fileName = strcat(CLIP_NAME, string(x), ".mp4");
    dvsTest(fileName, 640)
end

folderName = strcat("DVS", CLIP_NAME, "*");
folderList = dir(folderName);

status = mkdir(strcat("DVS", CLIP_NAME, "Frames"));
finalFolderDir = strcat(homeDir, "/", "DVS", CLIP_NAME, "Frames");

for x = 1:NUMBER_OF_CLIPS
    DVSfolderName = folderList(x).name;
    cd(DVSfolderName);
    DVSFrameList = dir("*.png");
    for y = 1:numel(DVSFrameList)
        status = movefile(DVSFrameList(y).name, finalFolderDir);
    end
    cd(homeDir);
    status = rmdir(DVSfolderName(4:end), 's');
    status = rmdir(DVSfolderName, 's');
    
end

clc;

%convert to RES x RES x 3



workingDir = pwd;
folderName = strcat("DVS", CLIP_NAME, "Frames");
cd(folderName);

framesList = dir('*.png');

oldPer = 0;

for x = 1 : numel(framesList)
    image = imread(framesList(x).name);
    image2 = zeros(1080, 1920, 3);
    image2(:, :, 1) = image;
    image2(:, :, 2) = image;
    image2(:, :, 3) = image;
    image = image2;
    image = imresize(image, [RES RES]);
    imwrite(image, framesList(x).name)
    newPer = round(100 * (x / numel(framesList)));
    if newPer > oldPer
        
    end
    oldPer = newPer;
end

clc;
disp("DVS Success!");