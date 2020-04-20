#include <stdio.h>
#include <stdbool.h>
unsigned short enc[100]; //Holds encoded array of integers representing each run (up to 100 runs, should be adjusted? as long as its > needed)
bool input[50] = {1,1,1,1,1 //1
                 ,1,1,1,1,1 //2
                 ,1,1,1,0,0 //3
                 ,0,0,0,0,0 //4
                 ,0,0,0,0,0 //5
                 ,0,0,0,0,0 //6
                 ,0,0,0,0,0 //7
                 ,0,0,1,1,1 //8
                 ,1,1,1,1,1 //9
                 ,1,0,0,0,1};//10 = 50 elements
                            //Every change from 1 to 0 or vice versa indicates the end of 1 run_len
                            //grab what the array starts with before using to fully decode properly
                 
bool *compress(bool *str) {
    bool *start = str;
    bool *c_first = str;
    bool *c_last = str;
    bool *c_write = str;
    int run_len = 0;
    int str_index = 0;
    int run_index = 0;
    //while (*str) { //breaks with boolean when 0, use string index instead and for loop/while over length of input (Which thankfully we know is fixed as frame size anyway)
    while (str_index <51) {   
        ++c_last; //push forward like worm ___
        ++run_len;
        if (*c_last != *c_first) { //if current bool is not the same as prev
            ////!(*c_last) || *c_last != *c_first
            // end of run
            if (run_len > 0)
                enc[run_index] = run_len;
            else
                enc[run_index] = 1; //run length was 1
            run_index++;
            //*(c_write++) = *c_first;
            
            // start next run
            run_len = 0; 
            c_first = c_last; //wiggle forward through input like worm _/\_
        }

        ++str; //to next input value
        ++str_index;
    }
    *c_write = 0;
    return start;
}
//int main(int argc, bool **argv)
int main() {
    //if (argc != 2)
    //    return 1;
    compress(&input[0]);
    
    // printing elements of encoded array
    for(int i = 0; i < 5; ++i) { //only printing 5 here because small input of 5 runs
     printf("%d\n", enc[i]);
    }
    return 0;
}
