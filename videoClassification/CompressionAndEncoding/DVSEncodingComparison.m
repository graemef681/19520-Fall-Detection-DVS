close all; clear;

% framesList = dir('*frame*.jpg');
% dvsList = dir('*dvs*.png');
% % LOSSLESS SOURCE CODING:
% %First Create Array of each, 2 normal frames and corresponding DVS frames.
% %Already Size Wise 
% %Frame 1 = [2091571]Bytes, Frame 2 = [2058274]Bytes. 
% %DVS1 = [151453]Bytes, DVS2 = [126986]Bytes
% %ThresholdBool1 = [102,400 bytes] ThresholdBool2 = [90,112 bytes] (Size on
% %Disk)
% %RLECoded = 84616bits = 10577bytes = 10.3kbs
% %Threshold DVS to be 1 and 0 instead of 255 and 0.
% frameArray = [];
% 
% for frameNum = 1:numel(framesList)
%    frameArray = cat(3,frameArray, rgb2gray(imread(framesList(frameNum).name))); 
% end
% 
% DVSArray = [];
% EncodeList = [0,0];
% SymbolProbList = [0,0;0,0];
% 
% for frameNum = 1:numel(dvsList)
%    DVSArray = cat(3,DVSArray, imread(dvsList(frameNum).name)); 
%    DVSEncode = DVSArray(:,:,frameNum);
%    DVSEncode = logical(DVSEncode);
%    imwrite(DVSEncode, sprintf('ThresholdBool%d.png', frameNum));
%    total_pixels = 2160*3840;
%    no_of_1 = sum(sum(DVSEncode));
%    SymbolProbList(frameNum,:) = [((total_pixels-no_of_1)/total_pixels),((no_of_1/total_pixels))];
%    H1a = -sum(SymbolProbList(frameNum,:).*log2(SymbolProbList(frameNum,:))); %Entropy of thresholded source = 0.1948 bits
%    [hcode, avg_len] = huffmandict([0,1],SymbolProbList(frameNum,:));
%    %encoded = huffmanenco(DVSEncode(:),hcode); %Encoded sequence 
%    %check = isequal(DVSEncode,encoded); %Sequence is the same, cannot be minimised as there are only 2 symbols. Total_Pixels number of bits still need sent
%    %Hence run length encode to shorten the data needed to be sent, then
%    %huffman for efficient encoding.
%    rle = rleenc(DVSEncode(:)); %Function splits 0 and 1s and shows which is which. Only the run set needs to be sent along with a header signaling a start of 1 or 0.
%    %Therefore only 84616 BITS need to be sent for this image, BEFORE any
%    %additional compression. The number of symbols representing the lenght
%    %of each run after this is highly inconsistent, however as the signal is
%    %binary already, RLE works extremely well for reducing the length of the
%    %sent signal. 
% end

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



%testimage = imcrop(testimage,[1000 1000.5 639 639]);
onedimage = reshape(testimage,[1 size(testimage,1)*size(testimage,2)]);
rlenc = rleenc(onedimage);
rldec = rledec(rlenc);
rldec(numel(onedimage)) = 0;
reconstruct = reshape(rldec,[640 640]);
figure(1);
imshow(testimage);
figure(2);
imshow(reconstruct);
payload = rlenc(:,2);
 % open your file for writing
 fid = fopen('myTextFile.txt','wt');
 % write the matrix
 
 if fid > 0
     fprintf(fid,'%o\n',payload');
     fclose(fid);
 end
%To Decode from RLE back to DVS Image. 
    %First Decode RLE to Binary thresholded Image.
    %Second, change brightness value to match required bit depth?
    %(Optional, logical pictures still produce black/white images).
%     %Fix Image dimensions from vector.
%     decodeBinary = rledec(rle);
%     for pixelNum = 1:numel(decodeBinary)
%         if(decodeBinary(pixelNum==1))
%             decodeBinary(pixelNum) = 255;
%         end
%     end
    %decodeImage = reshape(decodeBinary, [2160,3840]);
