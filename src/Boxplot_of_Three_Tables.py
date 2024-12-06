{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red245\green245\blue245;\red0\green0\blue0;
\red19\green85\blue52;\red144\green1\blue18;\red0\green0\blue255;\red101\green76\blue29;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c6667\c40000\c26667;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 data1 = [\cf5 \strokec5 10\cf0 \strokec4 , \cf5 \strokec5 20\cf0 \strokec4 , \cf5 \strokec5 30\cf0 \strokec4 , \cf5 \strokec5 40\cf0 \strokec4 , \cf5 \strokec5 50\cf0 \strokec4 ]\cb1 \
\cb3 data2 = [\cf5 \strokec5 15\cf0 \strokec4 , \cf5 \strokec5 25\cf0 \strokec4 , \cf5 \strokec5 35\cf0 \strokec4 , \cf5 \strokec5 45\cf0 \strokec4 , \cf5 \strokec5 55\cf0 \strokec4 ]\cb1 \
\cb3 data3 = [\cf5 \strokec5 5\cf0 \strokec4 , \cf5 \strokec5 15\cf0 \strokec4 , \cf5 \strokec5 25\cf0 \strokec4 , \cf5 \strokec5 35\cf0 \strokec4 , \cf5 \strokec5 45\cf0 \strokec4 ]\cb1 \
\
\cb3 data = [data1, data2, data3]\cb1 \
\
\cb3 box = plt.boxplot(data, labels=[\cf6 \strokec6 'Table 1'\cf0 \strokec4 , \cf6 \strokec6 'Table 2'\cf0 \strokec4 , \cf6 \strokec6 'Table 3'\cf0 \strokec4 ], patch_artist=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\cb3 colors = [\cf6 \strokec6 '#FF9999'\cf0 \strokec4 , \cf6 \strokec6 '#66B2FF'\cf0 \strokec4 , \cf6 \strokec6 '#99FF99'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  patch, color \cf7 \strokec7 in\cf0 \strokec4  \cf8 \cb3 \strokec8 zip\cf0 \cb3 \strokec4 (box[\cf6 \strokec6 'boxes'\cf0 \strokec4 ], colors):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     patch.set_facecolor(color)\cb1 \
\
\cb3 plt.title(\cf6 \strokec6 'Boxplot of Three Tables'\cf0 \strokec4 )\cb1 \
\cb3 plt.ylabel(\cf6 \strokec6 'Values'\cf0 \strokec4 )\cb1 \
\
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
\
\
}