/******************************************************************************/
/*                                                                            */
/* TCPEchoClient -- A DEIPcK TCP Client application to demonstrate how to use */
/*                  the TcpClient Class. This can be used in conjunction with */
/*                  TCPEchoServer.                                            */
/*                                                                            */
/******************************************************************************/
/* Author: Keith Vogel                                                        */
/* Copyright 2014, Digilent Inc.                                              */
/******************************************************************************/
/*
 *
 * Copyright (c) 2013-2014, Digilent <www.digilentinc.com>
 * Contact Digilent for the latest version.
 *
 * This program is free software; distributed under the terms of
 * BSD 3-clause license ("Revised BSD License", "New BSD License", or "Modified BSD License")
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * 1.    Redistributions of source code must retain the above copyright notice, this
 *        list of conditions and the following disclaimer.
 * 2.    Redistributions in binary form must reproduce the above copyright notice,
 *        this list of conditions and the following disclaimer in the documentation
 *        and/or other materials provided with the distribution.
 * 3.    Neither the name(s) of the above-listed copyright holder(s) nor the names
 *        of its contributors may be used to endorse or promote products derived
 *        from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */
/******************************************************************************/
/* Revision History:                                                          */
/*                                                                            */
/*    05/14/2014(KeithV):   Created                                           */
/*    08/09/2016(TommyK):   Modified to use Microblaze/Zynq                   */
/*    12/02/2017(atangzwj): Validated for Vivado 2016.4                       */
/*    01/20/2018(atangzwj): Validated for Vivado 2017.4                       */
/*                                                                            */
/******************************************************************************/

#include "PmodWIFI.h"
#include "xil_cache.h"
#include "xuartps.h"

#ifdef __MICROBLAZE__
#define PMODWIFI_VEC_ID XPAR_INTC_0_PMODWIFI_0_VEC_ID
#else
#define PMODWIFI_VEC_ID XPAR_FABRIC_PMODWIFI_0_WF_INTERRUPT_INTR
#endif

/************************************************************************/
/*                                                                      */
/*              SET THESE VALUES FOR YOUR NETWORK                       */
/*                                                                      */
/************************************************************************/

const char *szIPServer = "192.168.1.154"; // Server to connect to
//const char *szIPServer = "192.168.43.68"; // Server to connect to

//const char *szIPServer = "216.58.204.238"; //Port 80 for Google's servers
//IPv4 ipClient = {192,168,43,70};
uint16_t portServer = DEIPcK::iPersonalPorts44 + 300; // Port 44300
//uint16_t portServer = 80; // Port 44300

// Specify the SSID
const char *szSsid = "SSID";

// Select 1 for the security you want, or none for no security
#define USE_WPA2_PASSPHRASE
//#define USE_WPA2_KEY
//#define USE_WEP40
//#define USE_WEP104
//#define USE_WF_CONFIG_H

// Modify the security key to what you have.
#if defined(USE_WPA2_PASSPHRASE)

   const char *szPassPhrase = "PASSWORD";
   #define WiFiConnectMacro() deIPcK.wfConnect(szSsid, szPassPhrase, &status)

#elif defined(USE_WPA2_KEY)

   WPA2KEY key = { 0x27, 0x2C, 0x89, 0xCC, 0xE9, 0x56, 0x31, 0x1E,
                   0x3B, 0xAD, 0x79, 0xF7, 0x1D, 0xC4, 0xB9, 0x05,
                   0x7A, 0x34, 0x4C, 0x3E, 0xB5, 0xFA, 0x38, 0xC2,
                   0x0F, 0x0A, 0xB0, 0x90, 0xDC, 0x62, 0xAD, 0x58 };
   #define WiFiConnectMacro() deIPcK.wfConnect(szSsid, key, &status)

#elif defined(USE_WEP40)

   const int iWEPKey = 0;
   WEP40KEY keySet = { 0xBE, 0xC9, 0x58, 0x06, 0x97,   // Key 0
                       0x00, 0x00, 0x00, 0x00, 0x00,   // Key 1
                       0x00, 0x00, 0x00, 0x00, 0x00,   // Key 2
                       0x00, 0x00, 0x00, 0x00, 0x00 }; // Key 3
   #define WiFiConnectMacro() deIPcK.wfConnect(szSsid, keySet, iWEPKey, &status)

#elif defined(USE_WEP104)

   const int iWEPKey = 0;
   WEP104KEY keySet = { 0x3E, 0xCD, 0x30, 0xB2, 0x55, 0x2D, 0x3C, 0x50, 0x52, 0x71, 0xE8, 0x83, 0x91,   // Key 0
                        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,   // Key 1
                        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,   // Key 2
                        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 }; // Key 3
   #define WiFiConnectMacro() deIPcK.wfConnect(szSsid, keySet, iWEPKey, &status)

#elif defined(USE_WF_CONFIG_H)

   #define WiFiConnectMacro() deIPcK.wfConnect(0, &status)

#else // No security - OPEN

   #define WiFiConnectMacro() deIPcK.wfConnect(szSsid, &status)

#endif

//******************************************************************************************
//******************************************************************************************
//***************************** END OF CONFIGURATION ***************************************
//******************************************************************************************
//******************************************************************************************

typedef enum {
   NONE = 0,
   CONNECT,
   TCPCONNECT,
   WRITE,
   READ,
   CLOSE,
   DONE,
} STATE;

STATE state = CONNECT;

unsigned tStart = 0;
unsigned tWait = 100;

TCPSocket tcpSocket;
byte rgbRead[1024];

// This is for Print.write to print
byte rgbWrite[] = {'*','W','r','o','t','e',' ','f','r','o','m',' ','p','r','i','n','t','.','w','r','i','t','e','*','\n'};
int cbWrite = sizeof(rgbWrite);

// This is for tcpSocket.writeStream to print
byte rgbWriteStream[] = {'*','W','r','o','t','e',' ','f','r','o','m',' ','t','c','p','C','l','i','e','n','t','.','w','r','i','t','e','S','t','r','e','a','m','*','\n'};
int cbWriteStream = sizeof(rgbWriteStream);

/*** Global Variables ***/

const int width = 640;
const int height = 640;
u8 buffer[width*height*3];
int cbbuffer = sizeof(buffer);
int pixel_counter=0;



#define DEMO_PATTERN_0 0
#define DEMO_PATTERN_1 1
#define DEMO_MAX_FRAME (width*height*3)
#define DEMO_STRIDE (width * 3)
#define UART_BASEADDR 			XPAR_PS7_UART_1_BASEADDR
const int TCP_CLIENT_BUFFER = 1024;
void DemoInitialize();
void DemoRun();

void DemoPrintTest(u8 *frame, u32 width, u32 height, u32 stride, int pattern)
{
	u32 xcoi, ycoi;
	u32 iPixelAddr;
	u8 wRed, wBlue, wGreen;
	u32 wCurrentInt;
	double fRed, fBlue, fGreen, fColor;
	u32 xLeft, xMid, xRight, xInt;
	u32 yMid, yInt;
	double xInc, yInc;


	switch (pattern)
	{
	case DEMO_PATTERN_0:

		xInt = width / 4; //Four intervals, each with width/4 pixels
		xLeft = xInt * 3;
		xMid = xInt * 2 * 3;
		xRight = xInt * 3 * 3;
		xInc = 256.0 / ((double) xInt); //256 color intensities are cycled through per interval (overflow must be caught when color=256.0)

		yInt = height / 2; //Two intervals, each with width/2 lines
		yMid = yInt;
		yInc = 256.0 / ((double) yInt); //256 color intensities are cycled through per interval (overflow must be caught when color=256.0)

		fBlue = 0.0;
		fRed = 256.0;
		for(xcoi = 0; xcoi < (width*3); xcoi+=3)
		{
			/*
			 * Convert color intensities to integers < 256, and trim values >=256
			 */
			wRed = (fRed >= 256.0) ? 255 : ((u8) fRed);
			wBlue = (fBlue >= 256.0) ? 255 : ((u8) fBlue);
			iPixelAddr = xcoi;
			fGreen = 0.0;
			for(ycoi = 0; ycoi < height; ycoi++)
			{

				wGreen = (fGreen >= 256.0) ? 255 : ((u8) fGreen);
				frame[iPixelAddr] = wRed;
				frame[iPixelAddr + 1] = wBlue;
				frame[iPixelAddr + 2] = wGreen;
				if (ycoi < yMid)
				{
					fGreen += yInc;
				}
				else
				{
					fGreen -= yInc;
				}

				/*
				 * This pattern is printed one vertical line at a time, so the address must be incremented
				 * by the stride instead of just 1.
				 */
				iPixelAddr += stride;
			}

			if (xcoi < xLeft)
			{
				fBlue = 0.0;
				fRed -= xInc;
			}
			else if (xcoi < xMid)
			{
				fBlue += xInc;
				fRed += xInc;
			}
			else if (xcoi < xRight)
			{
				fBlue -= xInc;
				fRed -= xInc;
			}
			else
			{
				fBlue += xInc;
				fRed = 0;
			}
		}
		/*
		 * Flush the framebuffer memory range to ensure changes are written to the
		 * actual memory, and therefore accessible by the VDMA.
		 */
		Xil_DCacheFlushRange((unsigned int) frame, DEMO_MAX_FRAME);
		break;
	case DEMO_PATTERN_1:

		xInt = width / 7; //Seven intervals, each with width/7 pixels
		xInc = 256.0 / ((double) xInt); //256 color intensities per interval. Notice that overflow is handled for this pattern.

		fColor = 0.0;
		wCurrentInt = 1;
		for(xcoi = 0; xcoi < (width*3); xcoi+=3)
		{

			/*
			 * Just draw white in the last partial interval (when width is not divisible by 7)
			 */
			if (wCurrentInt > 7)
			{
				wRed = 255;
				wBlue = 255;
				wGreen = 255;
			}
			else
			{
				if (wCurrentInt & 0b001)
					wRed = (u8) fColor;
				else
					wRed = 0;

				if (wCurrentInt & 0b010)
					wBlue = (u8) fColor;
				else
					wBlue = 0;

				if (wCurrentInt & 0b100)
					wGreen = (u8) fColor;
				else
					wGreen = 0;
			}

			iPixelAddr = xcoi;

			for(ycoi = 0; ycoi < height; ycoi++)
			{
				frame[iPixelAddr] = wRed;
				frame[iPixelAddr + 1] = wBlue;
				frame[iPixelAddr + 2] = wGreen;
				/*
				 * This pattern is printed one vertical line at a time, so the address must be incremented
				 * by the stride instead of just 1.
				 */
				iPixelAddr += stride;
			}

			fColor += xInc;
			if (fColor >= 256.0)
			{
				fColor = 0.0;
				wCurrentInt++;
			}
		}
		/*
		 * Flush the framebuffer memory range to ensure changes are written to the
		 * actual memory, and therefore accessible by the VDMA.
		 */
		Xil_DCacheFlushRange((unsigned int) frame, DEMO_MAX_FRAME);
		break;
	default :
		xil_printf("Error: invalid pattern passed to DemoPrintTest");
	}
}


void ReadBuffer(u8 *destFrame, u32 width, u32 height, u32 stride)
{
	u32 xcoi, ycoi;
	u32 lineStart = 0;
	xil_printf("\n");
	for(ycoi = 0; ycoi < height; ycoi++)
	{
		for(xcoi = 0; xcoi < (width * 3); xcoi+=3)
		{
			xil_printf("destFrame = B 0x%02x | G 0x%02x | R 0x%02x \r\n",destFrame[xcoi + lineStart],destFrame[xcoi + lineStart + 1],destFrame[xcoi + lineStart + 2]);
		}
		lineStart += stride;
		if(lineStart==stride*2) break;
	}
	xil_printf("\nSize of buffer is: %d \n",sizeof(buffer));
}

void Menu(){
	char userInput = 0;
	char fRefresh; //flag used to trigger a refresh of the Menu on video detect

	/* Flush UART FIFO */
	while (XUartPs_IsReceiveData(UART_BASEADDR))
	{
		XUartPs_ReadReg(UART_BASEADDR, XUARTPS_FIFO_OFFSET);
	}

	while (userInput != 'q')
	{
		fRefresh = 0;

		/* Wait for data on UART */
		while (!XUartPs_IsReceiveData(UART_BASEADDR) && !fRefresh)
		{}

		/* Store the first character in the UART receive FIFO and echo it */
		if (XUartPs_IsReceiveData(UART_BASEADDR))
		{
			userInput = XUartPs_ReadReg(UART_BASEADDR, XUARTPS_FIFO_OFFSET);
			xil_printf("%c", userInput);
		}
		else  //Refresh triggered by video detect interrupt
		{
			userInput = 'r';
		}
		switch (userInput)
		{
		case '1':
			xil_printf("Data Transfer Initiated... \r\n");
			state=CONNECT;
			pixel_counter = 0;
			xil_printf("Success\r\n");
			break;

		case '2':
			xil_printf("Reading Buffer Initiated... \r\n");
			xil_printf("width: %d| height: %d| stride: %d",width,height,DEMO_STRIDE);
			ReadBuffer(buffer,width,height,DEMO_STRIDE);
			xil_printf("Success\r\n");
			break;
		default:
			break;
		}
	}
}

int main(void) {
   xil_printf("Main Start...\r\n");

   Xil_ICacheEnable();
   Xil_DCacheEnable();
   xil_printf("Writing Color Bar Test Pattern to Framebuffer...\r\n");
   DemoPrintTest(buffer, width, height, DEMO_STRIDE, DEMO_PATTERN_0); // This fills the buffer
   xil_printf("DONE Writing the Color Bar Test Pattern to Framebuffer...\r\n");

   xil_printf("WiFiTCPEchoClient 3.0\r\nConnecting to network...\r\n");
   DemoInitialize();
   DemoRun();

   return 0;
}

void DemoInitialize() {
   setPmodWifiAddresses(
      XPAR_PMODWIFI_0_AXI_LITE_SPI_BASEADDR,
      XPAR_PMODWIFI_0_AXI_LITE_WFGPIO_BASEADDR,
      XPAR_PMODWIFI_0_AXI_LITE_WFCS_BASEADDR,
      XPAR_PMODWIFI_0_S_AXI_TIMER_BASEADDR
   );
   setPmodWifiIntVector(PMODWIFI_VEC_ID);
}

void DemoRun() {
   IPSTATUS status;
   int cbRead = 0;
   byte Payload_buffer[TCP_CLIENT_BUFFER]; // Actual TCP Payload
   int i = 0;
   while (1) {
      switch (state) {
      case CONNECT:
         if (WiFiConnectMacro()) {
            xil_printf("WiFi connected\r\n");
            deIPcK.begin();
            state = TCPCONNECT;
         } else if (IsIPStatusAnError(status)) {
            xil_printf("Unable to connect, status: %d\r\n", status);
            state = CLOSE;
         }
         break;

      case TCPCONNECT:
    	 if (deIPcK.tcpConnect(szIPServer, portServer, tcpSocket)) {
            //xil_printf("Connected to server.\r\n");
            for(i=0;i<TCP_CLIENT_BUFFER-1;i++){
            	Payload_buffer[i]=buffer[i+pixel_counter];
            	// replace values in payload buffer with 1024 elements from the picture_buffer
            }
            //xil_printf("Filled the Payload_buffer.\r\n");
            //xil_printf("Pixel Counter = %d.\r\n",pixel_counter);
            pixel_counter=pixel_counter+TCP_CLIENT_BUFFER;
            state = WRITE;
         }
         break;

	 // Write out the strings
	 case WRITE:
		if (tcpSocket.isEstablished()) {
           //tcpSocket.writeStream(rgbWriteStream, cbWriteStream);
		   tcpSocket.writeStream(Payload_buffer, sizeof(Payload_buffer));
		   //xil_printf("Bytes Read Back:\r\n");
		   state = READ;
		   tStart = (unsigned) SYSGetMilliSecond();
		}
		break;

	 // Look for the echo back
	 case READ:

		// See if we got anything to read
		if ((cbRead = tcpSocket.available()) > 0) {
		   cbRead = cbRead < (int) sizeof(rgbRead) ? cbRead : sizeof(rgbRead);
		   cbRead = tcpSocket.readStream(rgbRead, cbRead);
		   rgbRead[cbRead] = 0; // Null Terminator
		   //xil_printf("%s\r\n", rgbRead);
		}

		// Give us some time to get everything echo'ed back
		else if ((((unsigned) SYSGetMilliSecond()) - tStart) > tWait) {
		   //xil_printf("\r\n");
		   state = CLOSE;
		}
		break;

      // Done, so close up the tcpSocket
      case CLOSE:
          if(pixel_counter<(width*height*3)) state = TCPCONNECT;
          else{
              xil_printf("Pixel Counter = %d.\r\n",pixel_counter);
              tcpSocket.close();
              xil_printf("Closing TcpClient, Done with sketch.\r\n");
              state = DONE;
          }
         break;

      case DONE:
    	  //break;
    	  if(!tcpSocket.isConnected()) Menu();
    	  //break;

      default:
         break;
      }

      // Keep the stack alive each pass through the loop()
      DEIPcK::periodicTasks();
   }
}
