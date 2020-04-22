function enc=rleenc(ins)
% rleenc - Run Length Encoding Algorithm
% rleenc - function performs run length encoding for binary input sequence.
% ins   - input sequence
% enc   - encoded output
%
% For example, x=randint(1,10,[0 1]); % Will give you a random sequence
% having only zeros and ones.
% enc=rleenc(x);
%
% developed by Suraj Kamya
% contact me: kamyasuraj@yahoo.com
% Encoding starts here
indx=find(ins);
len=length(indx);
ocnt=1; zcnt =0; enc=[]; strt=0;% One count, zero count, encoding sequence
for i=1:(len-1)
    % If sequence is starting with zeros
    if (indx(1)>1) && (strt==0);
       zcnt=indx(1)-1;
       enc=[enc;0,zcnt];
       zcnt=0; strt=1;
    end
    
    if (indx(i+1)-indx(i))==1
        ocnt=ocnt+1;
        up=0;
    else
        zcnt=indx(i+1)-indx(i)-1;
        enc=[enc;1,ocnt;0,zcnt];
        ocnt=1; zcnt=0;
        up=1; %Update pointer
    end
    
    % To update no. of one's if sequence is ended with one's;
    if (up==0) && (i==(len-1))
        enc=[enc;1,ocnt];
    end
end

