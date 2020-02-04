#include "DVS_source.hpp"
#include <hls_opencv.h>
#include <iostream>
#include <stdio.h>
using namespace std;
int main(int argc, char** argv){
	IplImage* src;
	IplImage* dst;
	AXI_STREAM src_axi, dst_axi;
	uint8_t a[180*320]={255};
	uint8_t b[180*320]={0};

	src = cvLoadImage("E:\5thYearDVS\DVS_IP\rocket.jpg");
	CvSize newsize = cvGetSize(src);
	dst = cvCreateImage(newsize, src->depth, src->nChannels);
	IplImage2AXIvideo(src,src_axi);
	DVS(src_axi, dst_axi, a, b);
	AXIvideo2IplImage(dst_axi, dst);
	cvSaveImage("E:\5thYearDVS\DVS_IP", dst);
	cvReleaseImage(&src);
	cvReleaseImage(&dst);

	return 0;
}
