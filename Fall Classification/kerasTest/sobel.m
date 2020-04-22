function sobel()
   framesList = dir('*.png');
   
   for x = 1 : numel(framesList)
      I = imread(framesList(x).name);
      I = edge(rgb2gray(I));
      imwrite(I, framesList(x).name);
   end
end