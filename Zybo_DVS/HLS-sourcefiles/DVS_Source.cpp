#include "DVS_Source.hpp"

void DVS(AXI_STREAM& INPUT_STREAM, AXI_STREAM& OUTPUT_STREAM, uint8_t readImage[57600], uint8_t writeImage[57600])
{
	#pragma HLS INTERFACE axis port=INPUT_STREAM
	#pragma HLS INTERFACE axis port=OUTPUT_STREAM
	#pragma HLS INTERFACE bram port=writeImage
	#pragma HLS INTERGACE bram port=readImage
	#pragma HLS RESOURCE variable=writeImage core=RAM_1P_BRAM
	#pragma HLS RESOURCE variable=readImage core=RAM_1P_BRAM

	RGB_IMAGE img_in(MAX_HEIGHT, MAX_WIDTH);
	GRAY_IMAGE img_grey(MAX_HEIGHT, MAX_WIDTH);
	H_IMAGE img_rs(QH, QW);
	H_IMAGE img_r(QH, QW);
	H_IMAGE img_dl(QH, QW);
	H_IMAGE img_p(QH, QW);
	H_IMAGE img_n(QH, QW);
	H_IMAGE img_f1(QH, QW);
	H_IMAGE img_f2(QH, QW);
	H_IMAGE img_add(QH, QW);
	H_IMAGE img_sub(QH, QW);
	H_IMAGE img_green(QH, QW);
	H_IMAGE img_red(QH, QW);
	H_IMAGE img_blue(QH, QW);
	GRAY_PIXEL pix_p(16);
	GRAY_PIXEL pix_n(16);
	GRAY_PIXEL pix_diff(17);
	H_IMAGE img_d2(QH, QW);
	H_IMAGE img_read(QH,QW);
	HRGB_IMAGE img(QH, QW);
	RGB_IMAGE img_final(MAX_HEIGHT, MAX_WIDTH);
	
	#pragma HLS dataflow
	hls::AXIvideo2Mat(INPUT_STREAM, img_in);
	hls::CvtColor<HLS_RGB2GRAY>(img_in, img_grey);
	hls::Resize(img_grey, img_r);
	hls::SubS(img_r, pix_diff, img_rs);
	hls::Duplicate(img_rs, img_dl, img_d2);
	hls::Array2Mat<QW, uint8_t, QH, QW, HLS_8UC1>(readImage, img_read);
	hls::Mat2Array<QW, uint8_t, QH, QW, HLS_8UC1>(img_d2, writeImage);
	hls::Duplicate(img_dl, img_p, img_n);
	hls::Duplicate(img_read, img_f1, img_f2);
	hls::AddS(img_f1, pix_p, img_add);
	hls::SubS(img_f2, pix_n, img_sub);
	hls::Cmp(img_p, img_add, img_green, HLS_CMP_GT);
	hls::Cmp(img_n, img_sub, img_red, HLS_CMP_LT);
	hls::Zero(img_blue);
	hls::Merge(img_green, img_blue, img_red, img);
	hls::Resize(img, img_final);
	hls::Mat2AXIvideo(img_final,OUTPUT_STREAM);
}
