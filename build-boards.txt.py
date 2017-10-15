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
#			resetmethod_ck/_nodemcu:	fixed reset method
#			flashmode_qio/_dio/_qout/_dout:	fixed flash mode
#			flashfreq_40/_80:		fixed flash frequency
#		selection menu:
#			resetmethod_menu		
#			crystalfreq/flashfreq_menu:	menus for selection crystal/flash frequency
#			flashmode_menu:			menus for flashmode selection (dio/dout/qio/qout)
#			512K/1M/2M/4M/8M/16M:		menus for flashsize / SPIFFS ratio

boards = [
	{
		'short': 'generic',
		'name': 'Generic ESP8266 Module',
		'opts': {
			'.build.board': 'ESP8266_GENERIC',
			},
		'macro': [
			'resetmethod_menu',
			'crystalfreq_menu',
			'flashfreq_menu',
			'flashmode_menu',
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
			'resetmethod_menu',
			'crystalfreq_menu',
			'flashmode_dout',
			'flashfreq_40',
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
			'resetmethod_ck',
			'flashmode_dio',
			'flashfreq_40',
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
			'resetmethod_nodemcu',
			'flashmode_qio',
			'flashfreq_40',
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
			'flashmode_dio',
			'flashfreq_40',
			'4M',
			'resetmethod_menu',
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
			'flashmode_dio',
			'flashfreq_40',
			'4M',
			'resetmethod_menu',
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
			'flashmode_dio',
			'flashfreq_40',
			'4M',
			'resetmethod_menu',
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
			'flashmode_dio',
			'flashfreq_40',
			'4M',
			'resetmethod_menu',
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
			'resetmethod_nodemcu',
			'flashmode_qio',
			'flashfreq_40',
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
			'resetmethod_nodemcu',
			'flashmode_dio',
			'flashfreq_40',
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
			'resetmethod_ck',
			'flashmode_qio',
			'flashfreq_40',
			'2M',
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
			'resetmethod_ck',
			'flashmode_qio',
			'flashfreq_40',
			'512K',
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
			'resetmethod_nodemcu',
			'flashmode_dio',
			'512K',
			],
	},
	{
		'short': 'esp210',
		'name': 'SweetPea ESP-210',
		'opts': {
			'.build.board': 'ESP8266_ESP210',
			},
		'macro': [
			'resetmethod_ck',
			'flashmode_qio',
			'flashfreq_40',
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
			'resetmethod_nodemcu',
			'flashmode_dio',
			'flashfreq_40',
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
			'resetmethod_nodemcu',
			'flashmode_dout',
			'flashfreq_40',
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
			'resetmethod_nodemcu',
			'flashmode_dio',
			'flashfreq_40',
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
			'flashmode_qio',
			'flashfreq_40',
			'4M',
			'resetmethod_menu',
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
			'resetmethod_nodemcu',
			'flashmode_qio',
			'flashfreq_40',
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
			'flashmode_qio',
			'flashfreq_menu',
			'flashfreq_40',
			'1M',
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
			'flashmode_qio',
			'flashfreq_40',
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
			'flashmode_qio',
			'flashfreq_80',
			'512K',
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
			'flashmode_dio',
			'flashfreq_40',
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
#useless	[ '.build.f_cpu', '80000000L' ],
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

	'cpufreq_menu': [
		[ '.menu.CpuFrequency.80', '80 MHz' ],
		[ '.menu.CpuFrequency.80.build.f_cpu', '80000000L' ],
		[ '.menu.CpuFrequency.160', '160 MHz' ],
		[ '.menu.CpuFrequency.160.build.f_cpu', '160000000L' ],
		],
	
	'crystalfreq_menu': [
		[ '.menu.CrystalFreq.26', '26 MHz' ],
		[ '.menu.CrystalFreq.40', '40 MHz' ],
		[ '.menu.CrystalFreq.40.build.extra_flags', '-DF_CRYSTAL=40000000' ],
		],
		
	'flashfreq_menu': [
		[ '.menu.FlashFreq.40', '40MHz' ],
		[ '.menu.FlashFreq.40.build.flash_freq', '40' ],
		[ '.menu.FlashFreq.80', '80MHz' ],
		[ '.menu.FlashFreq.80.build.flash_freq', '80' ],
		],
		
	'flashfreq_40': [
		[ '.build.flash_freq', '40' ],
		],

	'flashfreq_80': [
		[ '.build.flash_freq', '80' ],
		],

	####################### menu.resetmethod
	
	'resetmethod_menu': [
		[ '.menu.ResetMethod.ck', 'ck' ],
		[ '.menu.ResetMethod.ck.upload.resetmethod', 'ck' ],
		[ '.menu.ResetMethod.nodemcu', 'nodemcu' ],
		[ '.menu.ResetMethod.nodemcu.upload.resetmethod', 'nodemcu' ],
		],
	
	####################### upload.resetmethod
	
	'resetmethod_ck': [
		[ '.upload.resetmethod', 'ck' ],
		],
	
	'resetmethod_nodemcu': [
		[ '.upload.resetmethod', 'nodemcu' ],
		],

	####################### menu.FlashMode
	
	'flashmode_menu': [
		[ '.menu.FlashMode.qio', 'QIO' ],
		[ '.menu.FlashMode.qio.build.flash_mode', 'qio' ],
		[ '.menu.FlashMode.qout', 'QOUT' ],
		[ '.menu.FlashMode.qout.build.flash_mode', 'qout' ],
		[ '.menu.FlashMode.dio', 'DIO' ],
		[ '.menu.FlashMode.dio.build.flash_mode', 'dio' ],
		[ '.menu.FlashMode.dout', 'DOUT' ],
		[ '.menu.FlashMode.dout.build.flash_mode', 'dout' ],
		],

	####################### default flash_mode
	
	'flashmode_dio': [
		[ '.build.flash_mode', 'dio' ],
		],

	'flashmode_qio': [
		[ '.build.flash_mode', 'qio' ],
		],

	'flashmode_dout': [
		[ '.build.flash_mode', 'dout' ],
		],

	'flashmode_qout': [
		[ '.build.flash_mode', 'qout' ],
		],

	####################### debug

	'debug_menu': [
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

	####################### lwip

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

def flash_size (display, optname, ld, desc, max_upload_size, spiffs_start, spiffs_size, spiffs_blocksize):
	menu = '.menu.FlashSize.' + optname
	menub = menu + '.build.'
	d = [
		[ menu, display + ' (' + desc + ')' ],
		[ menub + 'flash_size', display ],
		[ menub + 'flash_ld', ld ],
		[ menub + 'spiffs_pagesize', '256' ],
		[ menu + '.upload.maximum_size', "%i" % max_upload_size ],
		]
	if spiffs_start > 0:
		d += [
			[ menub + 'spiffs_start', "0x%05X" % spiffs_start ],
			[ menub + 'spiffs_end', "0x%05X" % (spiffs_start + spiffs_size) ],
			[ menub + 'spiffs_blocksize', "%i" % spiffs_blocksize ],
			]
	return d
		
def all_flash_size ():
	return { '512K': 
		  flash_size('512K', '512K0',   'eagle.flash.512k0.ld',     'no SPIFFS', 499696, 0, 0, 0)
		+ flash_size('512K', '512K64',  'eagle.flash.512k64.ld',   '64K SPIFFS', 434160, 0x6B000, 0x10000, 4096)
		+ flash_size('512K', '512K128', 'eagle.flash.512k128.ld', '128K SPIFFS', 368624, 0x5B000, 0x20000, 4096)
		,
		'1M':
		  flash_size('1M', '1M0',   'eagle.flash.1m0.ld',     'no SPIFFS', 1023984, 0, 0, 0)
		+ flash_size('1M', '1M64',  'eagle.flash.1m64.ld',   '64K SPIFFS', 958448, 0xEB000, 0x10000, 4096)
		+ flash_size('1M', '1M128', 'eagle.flash.1m128.ld', '128K SPIFFS', 892912, 0xDB000, 0x20000, 4096)
		+ flash_size('1M', '1M144', 'eagle.flash.1m144.ld', '144K SPIFFS', 876528, 0xD7000, 0x24000, 4096)
		+ flash_size('1M', '1M160', 'eagle.flash.1m160.ld', '160K SPIFFS', 860144, 0xD3000, 0x28000, 4096)
		+ flash_size('1M', '1M192', 'eagle.flash.1m192.ld', '192K SPIFFS', 827376, 0xCB000, 0x30000, 4096)
		+ flash_size('1M', '1M256', 'eagle.flash.1m256.ld', '256K SPIFFS', 761840, 0xBB000, 0x40000, 4096)
		+ flash_size('1M', '1M512', 'eagle.flash.1m512.ld', '512K SPIFFS', 499696, 0x7B000, 0x80000, 8192)
		,
		'2M':
		  flash_size('2M', '2M', 'eagle.flash.2m.ld', '1M SPIFFS', 1044464, 0x100000,  0xFB000, 8192)
		,
		'4M':
		  flash_size('4M', '4M1M', 'eagle.flash.4m1m.ld', '1M SPIFFS', 1044464, 0x300000,  0xFB000, 8192)
		+ flash_size('4M', '4M3M', 'eagle.flash.4m.ld',   '3M SPIFFS', 1044464, 0x100000, 0x2FB000, 8192)
		,  
		'8M':
		  flash_size('8M', '8M7M', 'eagle.flash.8m.ld', '7M SPIFFS', 1044464, 0x100000, 0x6FB000, 8192)
		,
		'16M':
		  flash_size('16M', '16M15M', 'eagle.flash.16m.ld', '15M SPIFFS', 1044464, 0x100000, 0x16FB000, 8192)
		}

macros.update(all_flash_size())

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
	macrolist = [ 'defaults', 'cpufreq_menu', ]
	if 'macro' in board:
		macrolist += board['macro']
	macrolist += [ 'debug_menu' ]
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
