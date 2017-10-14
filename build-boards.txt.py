#!/usr/bin/env python

# boards.txt python builder for esp8266/Arduino
# Copyright (C) 2017 community
# Permission is hereby granted, free of charge, to any person who buy it,
# use it, break it, fix it, trash it, change it, mail - upgrade it, charge
# it, point it, zoom it, press it, snap it, work it, quick - erase it, write
# it, cut it, paste it, save it, load it, check it, quick - rewrite it, plug
# it, play it, burn it, rip it, drag and drop it, zip - unzip it, lock it,
# fill it, call it, find it, view it, code it, jam - unlock it, surf it,
# scroll it, pause it, click it, cross it, crack it, switch - update it,
# name it, rate it, tune it, print it, scan it, send it, fax - rename it,
# touch it, bring it, pay it, watch it, turn it, leave it, start - format
# it.

# board descriptor:
# 	short	short name
#	name	display name
#	opts:	specific entries dicts (overrides same entry in macros)
#	macro:	common entries
#		unmodifiable parameters:
#			f_ck/f_nodemcu:			fixed reset method
#			f_qio/f_dio/f_qout/f_dout:	fixed flash mode
#			f_512K/f_1M/f_2M/f_4M:		fixed flash size
#		selection menu:
#			crystalfreq/flashfreq:		menus for selection crystal/flash frequency
#			flashmode_io/flashmode_out:	menus for flashmode selection (dio/qio / dout/qout)
#			512K/1M/2M/4M:			menus for code/SPIFFS ratio

boards = [
	{
		'short': 'generic',
		'name': 'Generic ESP8266 Module',
		'opts': {
			'.build.board': 'ESP8266_GENERIC',
			},
		'macro': [
			'resetmethod',
			'cpufreq',
			'crystalfreq', 'flashfreq', 
			'flashmode_io', 'flashmode_out',
			'cpufreq',
			'512K', '1M', '2M', '4M', '8M', '16M',
			'lwip',
			],
	},
	{
		'short': 'esp8285',
		'name': 'Generic ESP8285 Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
			},
		'macro': [
			'f_ck',
			'f_dout',
			'f_ff40',
			'cpufreq',
			'1M',
			],
	},
	{
		'short': 'espduino',
		'name': 'ESPDuino (ESP-13 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			'.build.variant': 'ESPDuino',
			},
		'macro': [
			'f_ck',
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'huzzah',
		'name': 'Adafruit HUZZAH ESP8266',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			'.build.variant': 'adafruit',
			},
		'macro': [
			'f_nodemcu',
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'espresso_lite_v1',
		'name': 'ESPresso Lite 1.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V1',
			'.build.variant': 'espresso_lite_v1',
			},
		'macro': [
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			'resetmethod',
			],
	},
	{
		'short': 'espresso_lite_v2',
		'name': 'ESPresso Lite 2.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V2',
			'.build.variant': 'espresso_lite_v2',
			},
		'macro': [
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			'resetmethod',
			],
	},
	{
		'short': 'phoenix_v1',
		'name': 'Phoenix 1.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V1',
			'.build.variant': 'phoenix_v1',
			},
		'macro': [
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			'resetmethod',
			],
	},
	{
		'short': 'phoenix_v2',
		'name': 'Phoenix 2.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V2',
			'.build.variant': 'phoenix_v2',
			},
		'macro': [
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			'resetmethod',
			],
	},
	{
		'short': 'nodemcu',
		'name': 'NodeMCU 0.9 (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			'.build.variant': 'nodemcu',
			},
		'macro': [
			'f_nodemcu',
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'nodemcuv2',
		'name': 'NodeMCU 1.0 (ESP-12E Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			'.build.variant': 'nodemcu',
			},
		'macro': [
			'f_nodemcu',
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'modwifi',
		'name': 'Olimex MOD-WIFI-ESP8266(-DEV)',
		'opts': {
			'.build.board': 'MOD_WIFI_ESP8266',
			},
		'macro': [
			'f_ck',
			'f_qio',
			'f_ff40',
			'cpufreq',
			'f_2M',
			],
	},
	{
		'short': 'thing',
		'name': 'SparkFun ESP8266 Thing',
		'opts': {
			'.build.board': 'ESP8266_THING',
			'.build.variant': 'thing',
			},
		'macro': [
			'f_ck',
			'f_qio',
			'f_ff40',
			'cpufreq',
			'f_512K',
			],
	},
	{
		'short': 'thingdev',
		'name': 'SparkFun ESP8266 Thing Dev',
		'opts': {
			'.build.board': 'ESP8266_THING_DEV',
			'.build.variant': 'thingdev',
			},
		'macro': [
			'f_nodemcu',
			'f_dio',
			'cpufreq',
			'f_512K',
			],
	},
	{
		'short': 'esp210',
		'name': 'SweetPea ESP-210',
		'opts': {
			'.build.board': 'ESP8266_ESP210',
			},
		'macro': [
			'f_ck',
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'd1_mini',
		'name': 'WeMos D1 R2 & mini',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1R2MINI',
			'.build.variant': 'd1_mini',
			},
		'macro': [
			'f_nodemcu',
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'd1_mini_lite',
		'name': 'Wemos D1 mini lite',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1MINILITE',
			},
		'macro': [
			'f_nodemcu',
			'f_dout',
			'f_1M',
			'f_ff40',
			'cpufreq',
			'1M',
			],
	},
	{
		'short': 'd1',
		'name': 'WeMos D1 R1',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1R1',
			'.build.variant': 'd1',
			},
		'macro': [
			'f_nodemcu',
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'espino',
		'name': 'ESPino (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			'.build.variant': 'espino',
			},
		'macro': [
			#'f_ck',
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'flashmode_io',
			'4M',
			'resetmethod',
			]
	},
	{
		'short': 'espinotee',
		'name': 'ThaiEasyElec\'s ESPino',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			'.build.variant': 'espinotee',
			},
		'macro': [
			'f_nodemcu',
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'wifinfo',
		'name': 'WifInfo',
		'opts': {
			'.build.board': 'WIFINFO',
			'.build.variant': 'wifinfo',
			'.menu.ESPModule.ESP07192': 'ESP07 (1M/192K SPIFFS)',
			'.menu.ESPModule.ESP07192.build.board': 'ESP8266_ESP07',
			'.menu.ESPModule.ESP07192.build.flash_size': '1M',
			'.menu.ESPModule.ESP07192.build.flash_ld': 'eagle.flash.1m192.ld',
			'.menu.ESPModule.ESP07192.build.spiffs_start': '0xCB000',
			'.menu.ESPModule.ESP07192.build.spiffs_end': '0xFB000',
			'.menu.ESPModule.ESP07192.build.spiffs_blocksize': '4096',
			'.menu.ESPModule.ESP07192.upload.maximum_size': '827376',
			'.menu.ESPModule.ESP12': 'ESP12 (4M/1M SPIFFS)',
			'.menu.ESPModule.ESP12.build.board': 'ESP8266_ESP12',
			'.menu.ESPModule.ESP12.build.flash_size': '4M',
			'.menu.ESPModule.ESP12.build.flash_ld': 'eagle.flash.4m1m.ld',
			'.menu.ESPModule.ESP12.build.spiffs_start': '0x300000',
			'.menu.ESPModule.ESP12.build.spiffs_end': '0x3FB000',
			'.menu.ESPModule.ESP12.build.spiffs_blocksize': '8192',
			'.menu.ESPModule.ESP12.build.spiffs_pagesize': '256',
			'.menu.ESPModule.ESP12.upload.maximum_size': '1044464',
			},
		'macro': [
			'f_1M',
			'flashfreq',
			'flashmode_io',
			'f_ff40',
			'cpufreq',
			]
	},
	{
		'short': 'arduino-esp8266',
		'name': 'Arduino',
		'opts': {
			'.build.board': 'ESP8266_ARDUINO',
			'.menu.BoardModel.primo': 'Primo',
			'.menu.BoardModel.primo.build.board': 'ESP8266_ARDUINO_PRIMO',
			'.menu.BoardModel.primo.build.variant': 'arduino_spi',
			'.menu.BoardModel.primo.build.extra_flags': '-DF_CRYSTAL=40000000',
			'.menu.BoardModel.unowifideved': 'Uno WiFi',
			'.menu.BoardModel.unowifideved.build.board': 'ESP8266_ARDUINO_UNOWIFI',
			'.menu.BoardModel.unowifideved.build.variant': 'arduino_uart',
			'.menu.BoardModel.unowifideved.build.extra_flags=-DF_CRYSTAL': '40000000',
			'.menu.BoardModel.starottodeved': 'Star OTTO',
			'.menu.BoardModel.starottodeved.build.variant': 'arduino_uart',
			'.menu.BoardModel.starottodeved.build.board': 'ESP8266_ARDUINO_STAR_OTTO',
			'.menu.BoardModel.starottodeved.build.extra_flags': '-DF_CRYSTAL=40000000',
			},
		'macro': [
			'f_qio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	{
		'short': 'gen4iod',
		'name': '4D Systems gen4 IoD Range',
		'opts': {
			'.build.board': 'GEN4_IOD',
			'.build.f_cpu': '160000000L',
			},
		'macro': [
			'f_qio',
			'f_512K',
			'f_ff80',
			'cpufreq',
			],
	},
	{
		'short': 'oak',
		'name': 'DigiStump Oak',
		'opts': {
			'.build.board': 'ESP8266_OAK',
			'.build.variant': 'oak',
			'.upload.maximum_size': '1040368',
			},
		'macro': [
			'f_dio',
			'f_4M',
			'f_ff40',
			'cpufreq',
			'4M',
			],
	},
	]

################################################################

macros = {
	'defaults': [
		[ '.upload.tool', 'esptool' ],
		[ '.upload.speed', '115200' ],
		[ '.upload.maximum_data_size', '81920' ],
		[ '.upload.wait_for_upload_port', 'true' ],
		[ '.serial.disableDTR', 'true' ],
		[ '.serial.disableRTS', 'true' ],
		[ '.build.mcu', 'esp8266' ],
		[ '.build.f_cpu', '80000000L' ],
		[ '.build.core', 'esp8266' ],
		[ '.build.variant', 'generic' ],
		[ '.build.spiffs_pagesize', '256' ],
		[ '.build.debug_port', '' ],
		[ '.build.debug_level', '' ],

#lwip2:
#		[ '.build.lwip_include', 'lwip2/include' ],
#		[ '.build.lwip_lib', '-llwip2' ],

		],

	#######################

	'cpufreq': [
		[ '.menu.CpuFrequency.80', '80 MHz' ],
		[ '.menu.CpuFrequency.80.build.f_cpu', '80000000L' ],
		[ '.menu.CpuFrequency.160', '160 MHz' ],
		[ '.menu.CpuFrequency.160.build.f_cpu', '160000000L' ],
		],
	
	'crystalfreq': [
		[ '.menu.CrystalFreq.26', '26 MHz' ],
		[ '.menu.CrystalFreq.40', '40 MHz' ],
		[ '.menu.CrystalFreq.40.build.extra_flags', '-DF_CRYSTAL=40000000' ],
		],
		
	'flashfreq': [
		[ '.menu.FlashFreq.40', '40MHz' ],
		[ '.menu.FlashFreq.40.build.flash_freq', '40' ],
		[ '.menu.FlashFreq.80', '80MHz' ],
		[ '.menu.FlashFreq.80.build.flash_freq', '80' ],
		],
		
	'f_ff40': [
		[ '.build.flash_freq', '40' ],
		],

	'f_ff80': [
		[ '.build.flash_freq', '80' ],
		],

	####################### menu.resetmethod
	
	'resetmethod': [
		[ '.menu.ResetMethod.ck', 'ck' ],
		[ '.menu.ResetMethod.ck.upload.resetmethod', 'ck' ],
		[ '.menu.ResetMethod.nodemcu', 'nodemcu' ],
		[ '.menu.ResetMethod.nodemcu.upload.resetmethod', 'nodemcu' ],
		],
	
	####################### upload.resetmethod
	
	'f_ck': [
		[ '.upload.resetmethod', 'ck' ],
		],
	
	'f_nodemcu': [
		[ '.upload.resetmethod', 'nodemcu' ],
		],

	####################### menu.FlashSize

	'512K': [
		[ '.menu.FlashSize.512K0', '512K (no SPIFFS)' ],
		[ '.menu.FlashSize.512K0.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K0.build.flash_ld', 'eagle.flash.512k0.ld' ],
		[ '.menu.FlashSize.512K0.upload.maximum_size', '499696' ],
		[ '.menu.FlashSize.512K64', '512K (64K SPIFFS)' ],
		[ '.menu.FlashSize.512K64.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K64.build.flash_ld', 'eagle.flash.512k64.ld' ],
		[ '.menu.FlashSize.512K64.build.spiffs_start', '0x6B000' ],
		[ '.menu.FlashSize.512K64.build.spiffs_end', '0x7B000' ],
		[ '.menu.FlashSize.512K64.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.512K64.upload.maximum_size', '434160' ],
		[ '.menu.FlashSize.512K128', '512K (128K SPIFFS)' ],
		[ '.menu.FlashSize.512K128.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K128.build.flash_ld', 'eagle.flash.512k128.ld' ],
		[ '.menu.FlashSize.512K128.build.spiffs_start', '0x5B000' ],
		[ '.menu.FlashSize.512K128.build.spiffs_end', '0x7B000' ],
		[ '.menu.FlashSize.512K128.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.512K128.upload.maximum_size', '368624' ],
		],
	'1M': [
		[ '.menu.FlashSize.1M0', '1M (no SPIFFS)' ],
		[ '.menu.FlashSize.1M0.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M0.build.flash_ld', 'eagle.flash.1m0.ld' ],
		[ '.menu.FlashSize.1M0.upload.maximum_size', '1023984' ],
		[ '.menu.FlashSize.1M64', '1M (64K SPIFFS)' ],
		[ '.menu.FlashSize.1M64.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M64.build.flash_ld', 'eagle.flash.1m64.ld' ],
		[ '.menu.FlashSize.1M64.build.spiffs_start', '0xEB000' ],
		[ '.menu.FlashSize.1M64.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M64.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M64.upload.maximum_size', '958448' ],
		[ '.menu.FlashSize.1M128', '1M (128K SPIFFS)' ],
		[ '.menu.FlashSize.1M128.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M128.build.flash_ld', 'eagle.flash.1m128.ld' ],
		[ '.menu.FlashSize.1M128.build.spiffs_start', '0xDB000' ],
		[ '.menu.FlashSize.1M128.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M128.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M128.upload.maximum_size', '892912' ],
		[ '.menu.FlashSize.1M144', '1M (144K SPIFFS)' ],
		[ '.menu.FlashSize.1M144.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M144.build.flash_ld', 'eagle.flash.1m144.ld' ],
		[ '.menu.FlashSize.1M144.build.spiffs_start', '0xD7000' ],
		[ '.menu.FlashSize.1M144.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M144.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M144.upload.maximum_size', '876528' ],
		[ '.menu.FlashSize.1M160', '1M (160K SPIFFS)' ],
		[ '.menu.FlashSize.1M160.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M160.build.flash_ld', 'eagle.flash.1m160.ld' ],
		[ '.menu.FlashSize.1M160.build.spiffs_start', '0xD3000' ],
		[ '.menu.FlashSize.1M160.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M160.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M160.upload.maximum_size', '860144' ],
		[ '.menu.FlashSize.1M192', '1M (192K SPIFFS)' ],
		[ '.menu.FlashSize.1M192.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M192.build.flash_ld', 'eagle.flash.1m192.ld' ],
		[ '.menu.FlashSize.1M192.build.spiffs_start', '0xCB000' ],
		[ '.menu.FlashSize.1M192.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M192.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M192.upload.maximum_size', '827376' ],
		[ '.menu.FlashSize.1M256', '1M (256K SPIFFS)' ],
		[ '.menu.FlashSize.1M256.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M256.build.flash_ld', 'eagle.flash.1m256.ld' ],
		[ '.menu.FlashSize.1M256.build.spiffs_start', '0xBB000' ],
		[ '.menu.FlashSize.1M256.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M256.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M256.upload.maximum_size', '761840' ],
		[ '.menu.FlashSize.1M512', '1M (512K SPIFFS)' ],
		[ '.menu.FlashSize.1M512.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M512.build.flash_ld', 'eagle.flash.1m512.ld' ],
		[ '.menu.FlashSize.1M512.build.spiffs_start', '0x7B000' ],
		[ '.menu.FlashSize.1M512.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M512.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.1M512.upload.maximum_size', '499696' ],
		],
	'2M': [
		[ '.menu.FlashSize.2M', '2M (1M SPIFFS)' ],
		[ '.menu.FlashSize.2M.build.flash_size', '2M' ],
		[ '.menu.FlashSize.2M.build.flash_ld', 'eagle.flash.2m.ld' ],
		[ '.menu.FlashSize.2M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.2M.build.spiffs_end', '0x1FB000' ],
		[ '.menu.FlashSize.2M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.2M.upload.maximum_size', '1044464' ],
		],
	'4M': [
		[ '.menu.FlashSize.4M1M', '4M (1M SPIFFS)' ],
		[ '.menu.FlashSize.4M1M.build.flash_size', '4M' ],
		[ '.menu.FlashSize.4M1M.build.flash_ld', 'eagle.flash.4m1m.ld' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_start', '0x300000' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_end', '0x3FB000' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.4M1M.upload.maximum_size', '1044464' ],
		[ '.menu.FlashSize.4M3M', '4M (3M SPIFFS)' ],
		[ '.menu.FlashSize.4M3M.build.flash_size', '4M' ],
		[ '.menu.FlashSize.4M3M.build.flash_ld', 'eagle.flash.4m.ld' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_end', '0x3FB000' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.4M3M.upload.maximum_size', '1044464' ],
		],
	'8M': [
		[ '.menu.FlashSize.8M7M', '8M (7M SPIFFS)' ],
		[ '.menu.FlashSize.8M7M.build.flash_size', '8M' ],
		[ '.menu.FlashSize.8M7M.build.flash_ld', 'eagle.flash.8m.ld' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_end', '0x7FB000' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.8M7M.upload.maximum_size', '1044464' ],
		],
	'16M': [
		[ '.menu.FlashSize.16M15M', '16M (15M SPIFFS)' ],
		[ '.menu.FlashSize.16M15M.build.flash_size', '16M' ],
		[ '.menu.FlashSize.16M15M.build.flash_ld', 'eagle.flash.16m.ld' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_end', '0x17FB000' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.16M15M.upload.maximum_size', '1044464' ],
		],
	
	####################### default flash size
	
	'f_512K': [
		[ '.build.flash_size', '512k' ],
		[ '.upload.maximum_size', '434160' ],
		],
		
	'f_1M': [
		[ '.build.flash_size', '1M' ],
		[ '.upload.maximum_size', '1044464' ],
		],
		
	'f_2M': [
		[ '.build.flash_size', '2M' ],
		[ '.upload.maximum_size', '1044464' ],
		],
		
	'f_4M': [
		[ '.build.flash_size', '4M' ],
		[ '.upload.maximum_size', '1044464' ],
		],
	
	####################### menu.FlashMode
	
	'flashmode_io': [
		[ '.menu.FlashMode.dio', 'DIO' ],
		[ '.menu.FlashMode.dio.build.flash_mode', 'dio' ],
		[ '.menu.FlashMode.qio', 'QIO' ],
		[ '.menu.FlashMode.qio.build.flash_mode', 'qio' ],
		],
	
	'flashmode_out': [
		[ '.menu.FlashMode.dout', 'DOUT' ],
		[ '.menu.FlashMode.dout.build.flash_mode', 'dout' ],
		[ '.menu.FlashMode.qout', 'QOUT' ],
		[ '.menu.FlashMode.qout.build.flash_mode', 'qout' ],
		],

	####################### default flash_mode
	
	'f_dio': [
		[ '.build.flash_mode', 'dio' ],
		],

	'f_qio': [
		[ '.build.flash_mode', 'qio' ],
		],

	'f_dout': [
		[ '.build.flash_mode', 'dout' ],
		],

	'f_qout': [
		[ '.build.flash_mode', 'qout' ],
		],

	####################### debug

	'debug': [
		[ '.menu.Debug.Disabled', 'Disabled' ],
		[ '.menu.Debug.Disabled.build.debug_port', '' ],
		[ '.menu.Debug.Serial', 'Serial' ],
		[ '.menu.Debug.Serial.build.debug_port', '-DDEBUG_ESP_PORT=Serial' ],
		[ '.menu.Debug.Serial1', 'Serial1' ],
		[ '.menu.Debug.Serial1.build.debug_port', '-DDEBUG_ESP_PORT=Serial1' ],
		[ '.menu.DebugLevel.None____', 'None' ],
		[ '.menu.DebugLevel.None____.build.debug_level', '' ],
		[ '.menu.DebugLevel.Core____', 'Core' ],
		[ '.menu.DebugLevel.Core____.build.debug_level', '-DDEBUG_ESP_CORE' ],
		[ '.menu.DebugLevel.SSL_____', 'Core + SSL' ],
		[ '.menu.DebugLevel.SSL_____.build.debug_level', '-DDEBUG_ESP_CORE -DDEBUG_ESP_SSL' ],
		[ '.menu.DebugLevel.SSL_MEM_', 'Core + SSL + TLS Mem' ],
		[ '.menu.DebugLevel.SSL_MEM_.build.debug_level', '-DDEBUG_ESP_CORE -DDEBUG_ESP_SSL -DDEBUG_TLS_MEM' ],
		[ '.menu.DebugLevel.WiFic___', 'Core + WiFi' ],
		[ '.menu.DebugLevel.WiFic___.build.debug_level', '-DDEBUG_ESP_CORE -DDEBUG_ESP_WIFI' ],
		[ '.menu.DebugLevel.WiFi____', 'WiFi' ],
		[ '.menu.DebugLevel.WiFi____.build.debug_level', '-DDEBUG_ESP_WIFI' ],
		[ '.menu.DebugLevel.HTTPClient', 'HTTPClient' ],
		[ '.menu.DebugLevel.HTTPClient.build.debug_level', '-DDEBUG_ESP_HTTP_CLIENT' ],
		[ '.menu.DebugLevel.HTTPClient2', 'HTTPClient + SSL' ],
		[ '.menu.DebugLevel.HTTPClient2.build.debug_level', '-DDEBUG_ESP_HTTP_CLIENT -DDEBUG_ESP_SSL' ],
		[ '.menu.DebugLevel.HTTPUpdate', 'HTTPUpdate' ],
		[ '.menu.DebugLevel.HTTPUpdate.build.debug_level', '-DDEBUG_ESP_HTTP_UPDATE' ],
		[ '.menu.DebugLevel.HTTPUpdate2', 'HTTPClient + HTTPUpdate' ],
		[ '.menu.DebugLevel.HTTPUpdate2.build.debug_level', '-DDEBUG_ESP_HTTP_UPDATE -DDEBUG_ESP_HTTP_UPDATE' ],
		[ '.menu.DebugLevel.HTTPUpdate3', 'HTTPClient + HTTPUpdate + Updater' ],
		[ '.menu.DebugLevel.HTTPUpdate3.build.debug_level', '-DDEBUG_ESP_HTTP_UPDATE -DDEBUG_ESP_HTTP_UPDATE -DDEBUG_ESP_UPDATER' ],
		[ '.menu.DebugLevel.HTTPServer', 'HTTPServer' ],
		[ '.menu.DebugLevel.HTTPServer.build.debug_level', '-DDEBUG_ESP_HTTP_SERVER' ],
		[ '.menu.DebugLevel.UPDATER', 'Updater' ],
		[ '.menu.DebugLevel.UPDATER.build.debug_level', '-DDEBUG_ESP_UPDATER' ],
		[ '.menu.DebugLevel.OTA_____', 'OTA' ],
		[ '.menu.DebugLevel.OTA_____.build.debug_level', '-DDEBUG_ESP_OTA' ],
		[ '.menu.DebugLevel.OTA2____', 'OTA + Updater' ],
		[ '.menu.DebugLevel.OTA2____.build.debug_level', '-DDEBUG_ESP_OTA -DDEBUG_ESP_UPDATER' ],
		[ '.menu.DebugLevel.all_____', 'All' ],
		[ '.menu.DebugLevel.all_____.build.debug_level', '-DDEBUG_ESP_CORE -DDEBUG_ESP_SSL -DDEBUG_ESP_WIFI -DDEBUG_ESP_HTTP_CLIENT -DDEBUG_ESP_HTTP_UPDATE -DDEBUG_ESP_HTTP_SERVER -DDEBUG_ESP_UPDATER -DDEBUG_ESP_OTA -DDEBUG_TLS_MEM' ],
		],

	####################### debug

	'lwip': [
# lwip2:
#		[ '.menu.lwIPVariant.open', 'v2' ],
#		[ '.menu.lwIPVariant.open.build.lwip_include', 'lwip2/include' ],
#		[ '.menu.lwIPVariant.open.build.lwip_lib', '-llwip2' ],

		[ '.menu.LwIPVariant.Prebuilt', 'Prebuilt Source (gcc)' ],
		[ '.menu.LwIPVariant.Prebuilt.build.lwip_lib', '-llwip_gcc' ],
		[ '.menu.LwIPVariant.Prebuilt.build.lwip_flags', '-DLWIP_OPEN_SRC' ],
		[ '.menu.LwIPVariant.Espressif', 'Espressif (xcc)' ],
		[ '.menu.LwIPVariant.Espressif.build.lwip_lib', '-llwip' ],
		[ '.menu.LwIPVariant.Espressif.build.lwip_flags', '-DLWIP_MAYBE_XCC' ],
		[ '.menu.LwIPVariant.OpenSource', 'Open Source (gcc)' ],
		[ '.menu.LwIPVariant.OpenSource.build.lwip_lib', '-llwip_src' ],
		[ '.menu.LwIPVariant.OpenSource.build.lwip_flags', '-DLWIP_OPEN_SRC' ],
		[ '.menu.LwIPVariant.OpenSource.recipe.hooks.sketch.prebuild.1.pattern', 'make -C "{runtime.platform.path}/tools/sdk/lwip/src" install TOOLS_PATH="{runtime.tools.xtensa-lx106-elf-gcc.path}/bin/xtensa-lx106-elf-"' ],
		],

	}

################################################################

uploadspeed = [
		{ 'speed': 115200,	'os': [ '' ] }, 
		{ 'speed': 9600,	'os': [ '' ] },
		{ 'speed': 57600,	'os': [ '' ] },
		{ 'speed': 256000,	'os': [ '.windows' ] },
		{ 'speed': 230400,	'os': [ '.linux', '.macosx' ] },
		{ 'speed': 460800,	'os': [ '.linux', '.macosx' ] },
		{ 'speed': 512000,	'os': [ '.windows' ] },
		{ 'speed': 921600,	'os': [ '' ] },
		]

################################################################

print 'menu.BoardModel=Model'
print 'menu.UploadSpeed=Upload Speed'
print 'menu.CpuFrequency=CPU Frequency'
print 'menu.CrystalFreq=Crystal Frequency'
print 'menu.FlashSize=Flash Size'
print 'menu.FlashMode=Flash Mode'
print 'menu.FlashFreq=Flash Frequency'
print 'menu.ResetMethod=Reset Method'
print 'menu.ESPModule=Module'
print 'menu.Debug=Debug port'
print 'menu.DebugLevel=Debug Level'
print 'menu.LwIPVariant=lwIP Variant'
print 'menu.lwIP=lwIP Build'
print ''

for board in boards:
	print '##############################################################'
	short=board['short']
	print short + '.name=' + board['name']

	# standalone options
	if 'opts' in board:
		for opt in board['opts']:
			print short + opt + '=' + board['opts'][opt]
	
	# macros
	macrolist = [ 'defaults' ]
	if 'macro' in board:
		macrolist += board['macro']
	macrolist += [ 'debug' ]
	for block in macrolist:
		for keyval in macros[block]:
			if not ('opts' in board) or not (keyval[0] in board['opts']):
				print short + keyval[0] + '=' + keyval[1]

	# serial speed					
	for uspeed in uploadspeed:
		for os in uspeed['os']:
			speed=uspeed['speed']
			print short + '.menu.UploadSpeed.' + str(speed) + os + '=' + str(speed)
			print short + '.menu.UploadSpeed.' + str(speed) + '.upload.speed=' + str(speed)
	
	print ''
