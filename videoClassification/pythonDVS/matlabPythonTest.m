% 19520 Group Project - Group I
% Andrew Burr - 29/11/19
close all; clear;


folderPath = pwd;
scriptName = 'helloWorld.py';

commandStr = sprintf('python %s',scriptName);
[status, commandOut] = system(commandStr);
if status==0
    disp(commandOut);
end