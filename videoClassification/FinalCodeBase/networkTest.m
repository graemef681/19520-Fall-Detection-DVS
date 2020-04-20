close all; clear;


load('netTransfer-smallNetV4.mat');

% imdsTest = imageDatastore('fallData640testSmall10', ...
%     'IncludeSubfolders',true, ...
%     'LabelSource','foldernames');

[YPred,scores] = classify(netTransfer,imdsTest);

folderName = 'newDataset/fall';
YValidation = imdsTest.Labels;
accuracy = mean(YPred == YValidation);
accuracyPercent = accuracy * 100;

fprintf('Test Accuracy is %4.2f %% \n', accuracyPercent);

wrongPredictions = [];
for x = 1:numel(YPred)
    if(YPred(x) ~= YValidation(x))
        wrongPredictions = [wrongPredictions; x]; %#ok<AGROW>
    end
end

figure, set(gcf,'color','w'), confusionchart(YPred, YValidation);

images = [];
truths = [];
predicitions = [];
for x = 1:numel(wrongPredictions)
   tempImageName = cell2mat(imdsTest.Files(wrongPredictions(x)));
   tempImage = imread(tempImageName);
   tempTitle = strcat("Truth: ", string(YValidation(wrongPredictions(x))), "    Prediction: ", string(YPred(wrongPredictions(x))));
%    
%    figure;
%    imshow(tempImage);
%    text(30,30, tempTitle, 'color', 'r');
%    %title(tempTitle);
   
end

