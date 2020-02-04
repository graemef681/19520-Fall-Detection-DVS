#include "hls_video.h"
#include <ap_fixed.h>
#define MAX_WIDTH 1280
#define MAX_HEIGHT 720
#define QW 320
#define QH 180

typedef hls::stream<ap_axiu<24,1,1,1>>			AXI_STREAM;
typedef hls::Mat<MAX_HEIGHT, MAX_WIDTH, HLS_8UC3> RGB_IMAGE;
typedef hls::Mat<MAX_HEIGHT, MAX_WIDTH, HLS_8UC1> GRAY_IMAGE;
typedef hls::Scalar<1, unsigned char> GRAY_PIXEL;
typedef hls::Mat<QH, QW, HLS_8UC1> H_IMAGE;
typedef hls::Mat<QH, QW, HLS_8UC3> HRGB_IMAGE;
void DVS(AXI_STREAM& INPUT_STREAM, AXI_STREAM& OUTPUT_STREAM, uint8_t readImage[57600], uint8_t writeImage[57600]);
