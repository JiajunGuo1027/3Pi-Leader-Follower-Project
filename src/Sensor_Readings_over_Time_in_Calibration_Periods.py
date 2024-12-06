{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red245\green245\blue245;\red0\green0\blue0;
\red144\green1\blue18;\red19\green85\blue52;\red0\green0\blue255;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c6667\c40000\c26667;\cssrgb\c0\c0\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 file_path = \cf5 \strokec5 '/content/data1.xlsx'\cf0 \cb1 \strokec4 \
\cb3 sheet_name = \cf5 \strokec5 'data_1'\cf0 \cb1 \strokec4 \
\
\cb3 time_ms = df.iloc[:, \cf6 \strokec6 0\cf0 \strokec4 ]\cb1 \
\cb3 sensor_readings = df.iloc[:, \cf6 \strokec6 1\cf0 \strokec4 :]\cb1 \
\
\cb3 plt.figure(figsize=(\cf6 \strokec6 12\cf0 \strokec4 , \cf6 \strokec6 6\cf0 \strokec4 ))\cb1 \
\
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 0\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Bump Sensor_L'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 1\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Bump Sensor_R'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 2\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Line Sensor 1'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 3\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Line Sensor 2'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 4\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Line Sensor 3'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 5\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Line Sensor 4'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(time_ms, sensor_readings.iloc[:, \cf6 \strokec6 6\cf0 \strokec4 ], label=\cf7 \strokec7 f\cf5 \strokec5 'Line Sensor 5'\cf0 \strokec4 )\cb1 \
\
\cb3 plt.xlabel(\cf5 \strokec5 'Time (ms)'\cf0 \strokec4 )\cb1 \
\cb3 plt.ylabel(\cf5 \strokec5 'Sensor Reading'\cf0 \strokec4 )\cb1 \
\cb3 plt.title(\cf5 \strokec5 'Sensor Readings over Time in Calibration Periods'\cf0 \strokec4 , fontsize=\cf6 \strokec6 18\cf0 \strokec4 )\cb1 \
\cb3 plt.legend()\cb1 \
\cb3 plt.grid(\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3 plt.show()\cb1 \
}