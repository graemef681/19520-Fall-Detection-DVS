close all; clear;
% Requires:
% rledec.m
% encoded_BYTE{x}.txt
% 
%
% Script by: 
% Graeme Fitzpatrick
% University of Strathclyde

%Script will decode binary text file saved by python TCP Server containing
%DVS Image data from the FPGA.

%%Binary text file read 
fileID=fopen('encoded_BYTE4.txt');
array = fread(fileID);
data = zeros(1, (length(array)));

j=1;
for i=1:2:length(array)
   new_enc(j)=bi2de([de2bi(array(i),8,'left-msb'),de2bi(array(i+1),8,'left-msb')],'left-msb');
   j=j+1;
end

symbolslist = zeros(1, length(new_enc));
symbolslist(2:2:length(new_enc)) = 1;
new_enc = new_enc';
symbolslist = symbolslist';
dataenc(:,2) = new_enc;
dataenc(:,1) = symbolslist;

%Find first zero in encoded data, debug and confirmation of size needed to
%send image
%cutoff = find(dataenc(:,2)==0,1,'first');
%Trimmed function = new_enc(1:cutoff);
%noappendedzeros(:,1) = symbolslist(1:cutoff);
%noappendedzeros(:,2) = ToBeDecoded;

%Encoded data in format Ax2 where A(:,2) is encoded data and A(:,1) is
%symbols tied to each element. 
rldec = rledec(dataenc);
rldec(409600) = 0;
reconstruct = reshape(rldec,[640 640]);
figure(1);
%If image is rotated, transpose
imshow(reconstruct');
