{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red245\green245\blue245;\red0\green0\blue0;
\red19\green85\blue52;\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;\red15\green112\blue1;
\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c6667\c40000\c26667;\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c0\c50196\c0;
\cssrgb\c63922\c8235\c8235;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  numpy \cf2 \strokec2 as\cf0 \strokec4  np\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  scipy.optimize \cf2 \strokec2 import\cf0 \strokec4  curve_fit\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 x = np.array([\cf5 \strokec5 100\cf0 \strokec4 , \cf5 \strokec5 120\cf0 \strokec4 , \cf5 \strokec5 150\cf0 \strokec4 , \cf5 \strokec5 200\cf0 \strokec4 , \cf5 \strokec5 250\cf0 \strokec4 , \cf5 \strokec5 300\cf0 \strokec4 , \cf5 \strokec5 350\cf0 \strokec4 , \cf5 \strokec5 400\cf0 \strokec4 , \cf5 \strokec5 450\cf0 \strokec4 , \cf5 \strokec5 500\cf0 \strokec4 , \cf5 \strokec5 550\cf0 \strokec4 ])\cb1 \
\cb3 y = np.array([\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 5\cf0 \strokec4 , \cf5 \strokec5 15\cf0 \strokec4 , \cf5 \strokec5 16\cf0 \strokec4 , \cf5 \strokec5 17\cf0 \strokec4 , \cf5 \strokec5 18\cf0 \strokec4 , \cf5 \strokec5 19\cf0 \strokec4 , \cf5 \strokec5 20\cf0 \strokec4 , \cf5 \strokec5 25\cf0 \strokec4 , \cf5 \strokec5 28\cf0 \strokec4 , \cf5 \strokec5 32\cf0 \strokec4 ])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 linear_fit\cf0 \strokec4 (\cf8 \strokec8 x\cf0 \strokec4 , \cf8 \strokec8 a\cf0 \strokec4 , \cf8 \strokec8 b\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 return\cf0 \strokec4  a * x + b\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 quadratic_fit\cf0 \strokec4 (\cf8 \strokec8 x\cf0 \strokec4 , \cf8 \strokec8 a\cf0 \strokec4 , \cf8 \strokec8 b\cf0 \strokec4 , \cf8 \strokec8 c\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 return\cf0 \strokec4  a * x**\cf5 \strokec5 2\cf0 \strokec4  + b * x + c\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 cubic_fit\cf0 \strokec4 (\cf8 \strokec8 x\cf0 \strokec4 , \cf8 \strokec8 a\cf0 \strokec4 , \cf8 \strokec8 b\cf0 \strokec4 , \cf8 \strokec8 c\cf0 \strokec4 , \cf8 \strokec8 d\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 # print("a:",a,"b:",b,"c:",c,"d:",d)\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  a * x**\cf5 \strokec5 3\cf0 \strokec4  + b * x**\cf5 \strokec5 2\cf0 \strokec4  + c * x + d\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 exponential_fit\cf0 \strokec4 (\cf8 \strokec8 x\cf0 \strokec4 , \cf8 \strokec8 a\cf0 \strokec4 , \cf8 \strokec8 b\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 return\cf0 \strokec4  a * np.exp(b * x)\cb1 \
\
\cb3 popt_linear, pcov_linear = curve_fit(linear_fit, x, y)\cb1 \
\cb3 popt_quadratic, pcov_quadratic = curve_fit(quadratic_fit, x, y)\cb1 \
\cb3 popt_cubic, pcov_cubic = curve_fit(cubic_fit, x, y)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 try\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     popt_exponential, pcov_exponential = curve_fit(exponential_fit, x, y, p0=(\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 0.001\cf0 \strokec4 ))\cb1 \
\cb3     exponential_valid = \cf6 \strokec6 True\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 except\cf0 \strokec4  RuntimeError:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 print\cf0 \strokec4 (\cf10 \strokec10 "Exponential fit failed to converge."\cf0 \strokec4 )\cb1 \
\cb3     exponential_valid = \cf6 \strokec6 False\cf0 \cb1 \strokec4 \
\
\
\cb3 x_fit = np.linspace(\cf7 \strokec7 min\cf0 \strokec4 (x), \cf7 \strokec7 max\cf0 \strokec4 (x), \cf5 \strokec5 100\cf0 \strokec4 )\cb1 \
\
\cb3 plt.figure(figsize=(\cf5 \strokec5 10\cf0 \strokec4 , \cf5 \strokec5 6\cf0 \strokec4 ))\cb1 \
\cb3 plt.scatter(x, y, label=\cf10 \strokec10 'Original Data Points'\cf0 \strokec4 , color=\cf10 \strokec10 'blue'\cf0 \strokec4 )\cb1 \
\
\cb3 plt.plot(x_fit, linear_fit(x_fit, *popt_linear), label=\cf10 \strokec10 'Linear Fit'\cf0 \strokec4 , color=\cf10 \strokec10 'red'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(x_fit, quadratic_fit(x_fit, *popt_quadratic), label=\cf10 \strokec10 'Quadratic Fit'\cf0 \strokec4 , color=\cf10 \strokec10 'green'\cf0 \strokec4 )\cb1 \
\cb3 plt.plot(x_fit, cubic_fit(x_fit, *popt_cubic), label=\cf10 \strokec10 'Cubic Fit'\cf0 \strokec4 , color=\cf10 \strokec10 'orange'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  exponential_valid:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     plt.plot(x_fit, exponential_fit(x_fit, *popt_exponential), label=\cf10 \strokec10 'Exponential Fit'\cf0 \strokec4 , color=\cf10 \strokec10 'purple'\cf0 \strokec4 )\cb1 \
\
\cb3 plt.xlabel(\cf10 \strokec10 'Sensor Readings (Distance)'\cf0 \strokec4 )\cb1 \
\cb3 plt.ylabel(\cf10 \strokec10 'Expected Speed'\cf0 \strokec4 )\cb1 \
\cb3 plt.title(\cf10 \strokec10 'Curve Fitting with Different Functions'\cf0 \strokec4 ,fontsize=\cf5 \strokec5 18\cf0 \strokec4 )\cb1 \
\cb3 plt.legend()\cb1 \
\cb3 plt.grid(\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3 plt.show()\cb1 \
\
}