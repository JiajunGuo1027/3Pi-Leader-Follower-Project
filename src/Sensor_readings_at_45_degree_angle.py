{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red245\green245\blue245;\red0\green0\blue0;
\red19\green85\blue52;\red144\green1\blue18;\red15\green112\blue1;\red0\green0\blue255;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c6667\c40000\c26667;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  seaborn \cf2 \strokec2 as\cf0 \strokec4  sns\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 data1 = [\cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 872\cf0 \strokec4 , \cf5 \strokec5 821\cf0 \strokec4 , \cf5 \strokec5 730\cf0 \strokec4 , \cf5 \strokec5 718\cf0 \strokec4 , \cf5 \strokec5 802\cf0 \strokec4 , \cf5 \strokec5 854\cf0 \strokec4 , \cf5 \strokec5 844\cf0 \strokec4 , \cf5 \strokec5 856\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 875\cf0 \strokec4 , \cf5 \strokec5 809\cf0 \strokec4 , \cf5 \strokec5 838\cf0 \strokec4 , \cf5 \strokec5 793\cf0 \strokec4 , \cf5 \strokec5 797\cf0 \strokec4 , \cf5 \strokec5 810\cf0 \strokec4 , \cf5 \strokec5 808\cf0 \strokec4 , \cf5 \strokec5 810\cf0 \strokec4 , \cf5 \strokec5 808\cf0 \strokec4 , \cf5 \strokec5 808\cf0 \strokec4 , \cf5 \strokec5 809\cf0 \strokec4 , \cf5 \strokec5 810\cf0 \strokec4 , \cf5 \strokec5 809\cf0 \strokec4 ]\cb1 \
\cb3 data2 = [\cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 ]\cb1 \
\cb3 data3 = [\cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 ]\cb1 \
\cb3 data4 = [\cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 898\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 881\cf0 \strokec4 , \cf5 \strokec5 878\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 896\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 897\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 890\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 889\cf0 \strokec4 , \cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 ]\cb1 \
\cb3 data5 = [\cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 889\cf0 \strokec4 , \cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 884\cf0 \strokec4 , \cf5 \strokec5 877\cf0 \strokec4 , \cf5 \strokec5 866\cf0 \strokec4 , \cf5 \strokec5 864\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 882\cf0 \strokec4 , \cf5 \strokec5 882\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 882\cf0 \strokec4 , \cf5 \strokec5 875\cf0 \strokec4 , \cf5 \strokec5 878\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 ]\cb1 \
\cb3 data6 = [\cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 907\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 897\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 897\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 899\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 ]\cb1 \
\cb3 data7 = [\cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 917\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 ]\cb1 \
\
\cb3 data11 = [\cf5 \strokec5 833\cf0 \strokec4 , \cf5 \strokec5 844\cf0 \strokec4 , \cf5 \strokec5 840\cf0 \strokec4 , \cf5 \strokec5 833\cf0 \strokec4 , \cf5 \strokec5 828\cf0 \strokec4 , \cf5 \strokec5 772\cf0 \strokec4 , \cf5 \strokec5 707\cf0 \strokec4 , \cf5 \strokec5 704\cf0 \strokec4 , \cf5 \strokec5 705\cf0 \strokec4 , \cf5 \strokec5 756\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 946\cf0 \strokec4 , \cf5 \strokec5 973\cf0 \strokec4 , \cf5 \strokec5 978\cf0 \strokec4 , \cf5 \strokec5 967\cf0 \strokec4 , \cf5 \strokec5 954\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 793\cf0 \strokec4 , \cf5 \strokec5 715\cf0 \strokec4 , \cf5 \strokec5 717\cf0 \strokec4 , \cf5 \strokec5 831\cf0 \strokec4 , \cf5 \strokec5 953\cf0 \strokec4 , \cf5 \strokec5 960\cf0 \strokec4 , \cf5 \strokec5 959\cf0 \strokec4 , \cf5 \strokec5 961\cf0 \strokec4 , \cf5 \strokec5 965\cf0 \strokec4 , \cf5 \strokec5 964\cf0 \strokec4 , \cf5 \strokec5 961\cf0 \strokec4 , \cf5 \strokec5 961\cf0 \strokec4 , \cf5 \strokec5 963\cf0 \strokec4 , \cf5 \strokec5 961\cf0 \strokec4 , \cf5 \strokec5 973\cf0 \strokec4 , \cf5 \strokec5 973\cf0 \strokec4 , \cf5 \strokec5 973\cf0 \strokec4 , \cf5 \strokec5 973\cf0 \strokec4 ]\cb1 \
\cb3 data12 = [\cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 ,\cf5 \strokec5 1050\cf0 \strokec4 ,\cf5 \strokec5 1050\cf0 \strokec4 ,\cf5 \strokec5 1050\cf0 \strokec4 ]\cb1 \
\cb3 data13 = [\cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 926\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 928\cf0 \strokec4 , \cf5 \strokec5 927\cf0 \strokec4 , \cf5 \strokec5 929\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 930\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 ]\cb1 \
\cb3 data14 = [\cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 867\cf0 \strokec4 , \cf5 \strokec5 857\cf0 \strokec4 , \cf5 \strokec5 861\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 916\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 877\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 ]\cb1 \
\cb3 data15 = [\cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 887\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 877\cf0 \strokec4 , \cf5 \strokec5 860\cf0 \strokec4 , \cf5 \strokec5 849\cf0 \strokec4 , \cf5 \strokec5 853\cf0 \strokec4 , \cf5 \strokec5 875\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 868\cf0 \strokec4 , \cf5 \strokec5 868\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 ]\cb1 \
\cb3 data16 = [\cf5 \strokec5 907\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 915\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 ]\cb1 \
\cb3 data17 = [\cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 919\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 920\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 922\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 924\cf0 \strokec4 , \cf5 \strokec5 925\cf0 \strokec4 , \cf5 \strokec5 925\cf0 \strokec4 , \cf5 \strokec5 925\cf0 \strokec4 , \cf5 \strokec5 925\cf0 \strokec4 ]\cb1 \
\
\cb3 data21 = [\cf5 \strokec5 978\cf0 \strokec4 , \cf5 \strokec5 956\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 784\cf0 \strokec4 , \cf5 \strokec5 832\cf0 \strokec4 , \cf5 \strokec5 915\cf0 \strokec4 , \cf5 \strokec5 953\cf0 \strokec4 , \cf5 \strokec5 983\cf0 \strokec4 , \cf5 \strokec5 1012\cf0 \strokec4 , \cf5 \strokec5 1022\cf0 \strokec4 , \cf5 \strokec5 1005\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 821\cf0 \strokec4 , \cf5 \strokec5 791\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 940\cf0 \strokec4 , \cf5 \strokec5 970\cf0 \strokec4 , \cf5 \strokec5 984\cf0 \strokec4 , \cf5 \strokec5 981\cf0 \strokec4 , \cf5 \strokec5 951\cf0 \strokec4 , \cf5 \strokec5 923\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 872\cf0 \strokec4 , \cf5 \strokec5 801\cf0 \strokec4 , \cf5 \strokec5 765\cf0 \strokec4 , \cf5 \strokec5 830\cf0 \strokec4 , \cf5 \strokec5 872\cf0 \strokec4 , \cf5 \strokec5 907\cf0 \strokec4 , \cf5 \strokec5 941\cf0 \strokec4 , \cf5 \strokec5 963\cf0 \strokec4 , \cf5 \strokec5 987\cf0 \strokec4 , \cf5 \strokec5 997\cf0 \strokec4 , \cf5 \strokec5 981\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 865\cf0 \strokec4 ]\cb1 \
\cb3 data22 = [\cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 1050\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 ,  \cf5 \strokec5 850\cf0 \strokec4 ]\cb1 \
\cb3 data23 = [\cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 937\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 937\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 937\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 937\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 931\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 932\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 935\cf0 \strokec4 , \cf5 \strokec5 938\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 934\cf0 \strokec4 , \cf5 \strokec5 936\cf0 \strokec4 , \cf5 \strokec5 933\cf0 \strokec4 ]\cb1 \
\cb3 data24 = [\cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 907\cf0 \strokec4 , \cf5 \strokec5 897\cf0 \strokec4 , \cf5 \strokec5 876\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 898\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 921\cf0 \strokec4 , \cf5 \strokec5 917\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 882\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 875\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 896\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 916\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 901\cf0 \strokec4 , \cf5 \strokec5 891\cf0 \strokec4 ]\cb1 \
\cb3 data25 = [\cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 870\cf0 \strokec4 , \cf5 \strokec5 845\cf0 \strokec4 , \cf5 \strokec5 853\cf0 \strokec4 , \cf5 \strokec5 873\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 904\cf0 \strokec4 , \cf5 \strokec5 899\cf0 \strokec4 , \cf5 \strokec5 881\cf0 \strokec4 , \cf5 \strokec5 853\cf0 \strokec4 , \cf5 \strokec5 845\cf0 \strokec4 , \cf5 \strokec5 868\cf0 \strokec4 , \cf5 \strokec5 881\cf0 \strokec4 , \cf5 \strokec5 890\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 894\cf0 \strokec4 , \cf5 \strokec5 886\cf0 \strokec4 , \cf5 \strokec5 876\cf0 \strokec4 , \cf5 \strokec5 873\cf0 \strokec4 , \cf5 \strokec5 864\cf0 \strokec4 , \cf5 \strokec5 847\cf0 \strokec4 , \cf5 \strokec5 842\cf0 \strokec4 , \cf5 \strokec5 855\cf0 \strokec4 , \cf5 \strokec5 864\cf0 \strokec4 , \cf5 \strokec5 870\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 889\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 899\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 862\cf0 \strokec4 ]\cb1 \
\cb3 data26 = [\cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 895\cf0 \strokec4 , \cf5 \strokec5 879\cf0 \strokec4 , \cf5 \strokec5 849\cf0 \strokec4 , \cf5 \strokec5 861\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 893\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 916\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 889\cf0 \strokec4 , \cf5 \strokec5 859\cf0 \strokec4 , \cf5 \strokec5 850\cf0 \strokec4 , \cf5 \strokec5 875\cf0 \strokec4 , \cf5 \strokec5 888\cf0 \strokec4 , \cf5 \strokec5 900\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 892\cf0 \strokec4 , \cf5 \strokec5 883\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 871\cf0 \strokec4 , \cf5 \strokec5 854\cf0 \strokec4 , \cf5 \strokec5 847\cf0 \strokec4 , \cf5 \strokec5 860\cf0 \strokec4 , \cf5 \strokec5 871\cf0 \strokec4 , \cf5 \strokec5 880\cf0 \strokec4 , \cf5 \strokec5 889\cf0 \strokec4 , \cf5 \strokec5 898\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 885\cf0 \strokec4 , \cf5 \strokec5 869\cf0 \strokec4 ]\cb1 \
\cb3 data27 = [\cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 915\cf0 \strokec4 , \cf5 \strokec5 918\cf0 \strokec4 , \cf5 \strokec5 916\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 905\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 907\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 913\cf0 \strokec4 , \cf5 \strokec5 912\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 909\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 903\cf0 \strokec4 , \cf5 \strokec5 902\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 , \cf5 \strokec5 908\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 911\cf0 \strokec4 , \cf5 \strokec5 915\cf0 \strokec4 , \cf5 \strokec5 914\cf0 \strokec4 , \cf5 \strokec5 915\cf0 \strokec4 , \cf5 \strokec5 910\cf0 \strokec4 , \cf5 \strokec5 906\cf0 \strokec4 ]\cb1 \
\
\cb3 df = pd.DataFrame(\{\cb1 \
\cb3     \cf6 \strokec6 'Bump_L'\cf0 \strokec4 : data1,\cb1 \
\cb3     \cf6 \strokec6 'Bump_R'\cf0 \strokec4 : data2,\cb1 \
\cb3     \cf6 \strokec6 'Line_1'\cf0 \strokec4 : data3,\cb1 \
\cb3     \cf6 \strokec6 'Line_2'\cf0 \strokec4 : data4,\cb1 \
\cb3     \cf6 \strokec6 'Line_3'\cf0 \strokec4 : data5,\cb1 \
\cb3     \cf6 \strokec6 'Line_4'\cf0 \strokec4 : data6,\cb1 \
\cb3     \cf6 \strokec6 'Line_5'\cf0 \strokec4 : data7\cb1 \
\cb3 \})\cb1 \
\cb3 df2 = pd.DataFrame(\{\cb1 \
\cb3     \cf6 \strokec6 'Bump_L'\cf0 \strokec4 : data11,\cb1 \
\cb3     \cf6 \strokec6 'Bump_R'\cf0 \strokec4 : data12,\cb1 \
\cb3     \cf6 \strokec6 'Line_1'\cf0 \strokec4 : data13,\cb1 \
\cb3     \cf6 \strokec6 'Line_2'\cf0 \strokec4 : data14,\cb1 \
\cb3     \cf6 \strokec6 'Line_3'\cf0 \strokec4 : data15,\cb1 \
\cb3     \cf6 \strokec6 'Line_4'\cf0 \strokec4 : data16,\cb1 \
\cb3     \cf6 \strokec6 'Line_5'\cf0 \strokec4 : data17\cb1 \
\cb3 \})\cb1 \
\cb3 df3 = pd.DataFrame(\{\cb1 \
\cb3     \cf6 \strokec6 'Bump_L'\cf0 \strokec4 : data21,\cb1 \
\cb3     \cf6 \strokec6 'Bump_R'\cf0 \strokec4 : data22,\cb1 \
\cb3     \cf6 \strokec6 'Line_1'\cf0 \strokec4 : data23,\cb1 \
\cb3     \cf6 \strokec6 'Line_2'\cf0 \strokec4 : data24,\cb1 \
\cb3     \cf6 \strokec6 'Line_3'\cf0 \strokec4 : data25,\cb1 \
\cb3     \cf6 \strokec6 'Line_4'\cf0 \strokec4 : data26,\cb1 \
\cb3     \cf6 \strokec6 'Line_5'\cf0 \strokec4 : data27\cb1 \
\cb3 \})\cb1 \
\
\cb3 df_melted = df.melt(var_name=\cf6 \strokec6 'Sensors'\cf0 \strokec4 , value_name=\cf6 \strokec6 'Readings'\cf0 \strokec4 )\cb1 \
\cb3 df2_melted = df2.melt(var_name=\cf6 \strokec6 'Sensors'\cf0 \strokec4 , value_name=\cf6 \strokec6 'Readings'\cf0 \strokec4 )\cb1 \
\cb3 df3_melted = df3.melt(var_name=\cf6 \strokec6 'Sensors'\cf0 \strokec4 , value_name=\cf6 \strokec6 'Readings'\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # custom_palette = ['#FF9999', '#66B2FF', '#99FF99']\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7 # #plt.figure(figsize=(4, 6))\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7 # sns.boxplot(x='Table', y='Values', data=df_melted, palette=custom_palette)\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7 # plt.title('Boxplot of Three Tables', fontsize=14)\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # plt.xlabel('Tables', fontsize=12)\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # plt.ylabel('Values', fontsize=12)\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7 # #plt.tight_layout()\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # plt.show()\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 group1 = df_melted[df_melted[\cf6 \strokec6 'Sensors'\cf0 \strokec4 ].isin([\cf6 \strokec6 'Bump_L'\cf0 \strokec4 , \cf6 \strokec6 'Bump_R'\cf0 \strokec4 , \cf6 \strokec6 'Line_1'\cf0 \strokec4 , \cf6 \strokec6 'Line_2'\cf0 \strokec4 , \cf6 \strokec6 'Line_3'\cf0 \strokec4 , \cf6 \strokec6 'Line_4'\cf0 \strokec4 , \cf6 \strokec6 'Line_5'\cf0 \strokec4 ])]\cb1 \
\cb3 group2 = df2_melted[df_melted[\cf6 \strokec6 'Sensors'\cf0 \strokec4 ].isin([\cf6 \strokec6 'Bump_L'\cf0 \strokec4 , \cf6 \strokec6 'Bump_R'\cf0 \strokec4 , \cf6 \strokec6 'Line_1'\cf0 \strokec4 , \cf6 \strokec6 'Line_2'\cf0 \strokec4 , \cf6 \strokec6 'Line_3'\cf0 \strokec4 , \cf6 \strokec6 'Line_4'\cf0 \strokec4 , \cf6 \strokec6 'Line_5'\cf0 \strokec4 ])]\cb1 \
\cb3 group3 = df3_melted[df_melted[\cf6 \strokec6 'Sensors'\cf0 \strokec4 ].isin([\cf6 \strokec6 'Bump_L'\cf0 \strokec4 , \cf6 \strokec6 'Bump_R'\cf0 \strokec4 , \cf6 \strokec6 'Line_1'\cf0 \strokec4 , \cf6 \strokec6 'Line_2'\cf0 \strokec4 , \cf6 \strokec6 'Line_3'\cf0 \strokec4 , \cf6 \strokec6 'Line_4'\cf0 \strokec4 , \cf6 \strokec6 'Line_5'\cf0 \strokec4 ])]\cb1 \
\
\cb3 custom_palette = [\cf6 \strokec6 '#FF9999'\cf0 \strokec4 , \cf6 \strokec6 '#66B2FF'\cf0 \strokec4 , \cf6 \strokec6 '#99FF99'\cf0 \strokec4 , \cf6 \strokec6 '#FFCC99'\cf0 \strokec4 , \cf6 \strokec6 '#99CCFF'\cf0 \strokec4 , \cf6 \strokec6 '#66FFCC'\cf0 \strokec4 , \cf6 \strokec6 '#CC99FF'\cf0 \strokec4 ]\cb1 \
\
\cb3 fig, axes = plt.subplots(\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 2\cf0 \strokec4 , figsize=(\cf5 \strokec5 18\cf0 \strokec4 , \cf5 \strokec5 6\cf0 \strokec4 ), sharey=\cf8 \strokec8 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # sns.boxplot(x='Sensors', y='Readings', data=group1, palette=custom_palette[:3], ax=axes[0])\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # axes[0].set_title('Distance Deviation during the Stopping Phase')\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # axes[0].set_xlabel('Sensors')\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # axes[0].set_ylabel('Readings')\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sns.boxplot(x=\cf6 \strokec6 'Sensors'\cf0 \strokec4 , y=\cf6 \strokec6 'Readings'\cf0 \strokec4 , data=group2, palette=custom_palette[\cf5 \strokec5 3\cf0 \strokec4 :\cf5 \strokec5 5\cf0 \strokec4 ], ax=axes[\cf5 \strokec5 0\cf0 \strokec4 ])\cb1 \
\cb3 axes[\cf5 \strokec5 0\cf0 \strokec4 ].set_title(\cf6 \strokec6 'Sensor readings at a 45-degree angle between the two robots'\cf0 \strokec4 , fontsize=\cf5 \strokec5 19\cf0 \strokec4 )\cb1 \
\cb3 axes[\cf5 \strokec5 0\cf0 \strokec4 ].set_xlabel(\cf6 \strokec6 'Sensors'\cf0 \strokec4 )\cb1 \
\
\cb3 sns.boxplot(x=\cf6 \strokec6 'Sensors'\cf0 \strokec4 , y=\cf6 \strokec6 'Readings'\cf0 \strokec4 , data=group3, palette=custom_palette[\cf5 \strokec5 5\cf0 \strokec4 :], ax=axes[\cf5 \strokec5 1\cf0 \strokec4 ])\cb1 \
\cb3 axes[\cf5 \strokec5 1\cf0 \strokec4 ].set_title(\cf6 \strokec6 'Sensor readings at a -45-degree angle between the two robots'\cf0 \strokec4 ,fontsize=\cf5 \strokec5 19\cf0 \strokec4 )\cb1 \
\cb3 axes[\cf5 \strokec5 1\cf0 \strokec4 ].set_xlabel(\cf6 \strokec6 'Sensors'\cf0 \strokec4 )\cb1 \
\
\cb3 plt.tight_layout()\cb1 \
\
\cb3 plt.show()\cb1 \
\
}