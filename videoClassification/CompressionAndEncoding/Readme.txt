Bug currently with debugging RLE, easy fix. 
Loads data, images are already huffman coded via imwrite, however they are 8bit unsigned with [0,255] as symbols. Converts to boolean [0,1] to compress storage
and encodes with RLE to compress further losslessly. Sent data is only a few kbs. 
