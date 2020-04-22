function dec=rledec(enc)
% rledec - Run Length Decoding Algorithm
% rledec - function performs run length decoding for binary coded sequence.
% enc    - encoded input
% dec    - decoded output
%
% For example, x =[0     0     1     1     1     0     1     0     0     0
% 1     1];
%enc=rleenc(x)
%enc =
% 
%      0     2
%      1     3
%      0     1
%      1     1
%      0     3
%      1     2
% dec=rledec(enc);
%
% developed by Suraj Kamya
% contact me: kamyasuraj@yahoo.com
enc=enc'; enc=enc(:); %Converting in row vector
 len=length(enc);
 dec=[]; %decoding sequence
 for i=1:2:len
     dec=[dec,(ones(1,enc(i+1)))*enc(i)];
 end