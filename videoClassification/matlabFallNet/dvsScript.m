NUMBER_OF_CLIPS = 92;
CLIP_NAME = "fall";

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
disp("DVS Success!");