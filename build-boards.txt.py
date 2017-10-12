#!/usr/bin/env python

defaults = [
		[ '.upload.tool', 'esptool' ],
		[ '.upload.speed', '115200' ],
		[ '.upload.resetmethod', 'ck' ],
		[ '.upload.maximum_size', '434160' ],
		[ '.upload.maximum_data_size', '81920' ],
		[ '.upload.wait_for_upload_port', 'true' ],
		[ '.serial.disableDTR', 'true' ],
		[ '.serial.disableRTS', 'true' ],
		[ '.build.mcu', 'esp8266' ],
		[ '.build.f_cpu', '80000000L' ],
		[ '.build.core', 'esp8266' ],
		[ '.build.variant', 'generic' ],
		[ '.build.flash_mode', 'qio' ],
		[ '.build.spiffs_pagesize', '256' ],
		[ '.build.debug_port', '' ],
		[ '.build.debug_level', '' ],
	]

boards = [
	{
		'short': 'generic',
		'name': 'Generic ESP8266 Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
## flash_mode should be defined elsewhere and merged (in 'opts') where appropriate, how do we easily merge in python?
			'.menu.FlashMode.dio.build.flash_mode': 'dio',
			'.menu.FlashMode.qio.build.flash_mode': 'qio',
			'.menu.FlashMode.dout.build.flash_mode': 'dout',
			'.menu.FlashMode.qout.build.flash_mode': 'qout',
			}
	},
	{
		'short': 'esp8285',
		'name': 'Generic ESP8285 Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
			'.build.flash_mode': 'dout',
			}
	},
	{
		'short': 'espduino',
		'name': 'ESPDuino (ESP-13 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'huzzah',
		'name': 'Adafruit HUZZAH ESP8266',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			}
	},
	{
		'short': 'espresso_lite_v1',
		'name': 'ESPresso Lite 1.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V1',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'espresso_lite_v2',
		'name': 'ESPresso Lite 2.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V2',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'phoenix_v1',
		'name': 'Phoenix 1.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V1',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'phoenix_v2',
		'name': 'Phoenix 2.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V2',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'nodemcu',
		'name': 'NodeMCU 0.9 (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			}
	},
	{
		'short': 'nodemcuv2',
		'name': 'NodeMCU 1.0 (ESP-12E Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'modwifi',
		'name': 'Olimex MOD-WIFI-ESP8266(-DEV)',
		'opts': {
			'.build.board': 'MOD_WIFI_ESP8266',
			}
	},
	{
		'short': 'thing',
		'name': 'SparkFun ESP8266 Thing',
		'opts': {
			'.build.board': 'ESP8266_THING',
			}
	},
	{
		'short': 'thingdev',
		'name': 'SparkFun ESP8266 Thing Dev',
		'opts': {
			'.build.board': 'ESP8266_THING_DEV',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'esp210',
		'name': 'SweetPea ESP-210',
		'opts': {
			'.build.board': 'ESP8266_ESP210',
			}
	},
	{
		'short': 'd1_mini',
		'name': 'WeMos D1 R2 & mini',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1R2MINI',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'd1_mini_lite',
		'name': 'Wemos D1 mini lite (ESP8285)',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1MINILITE',
			'.build.flash_mode': 'dout',
			}
	},
	{
		'short': 'd1',
		'name': 'WeMos D1 R1',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1R1',
			'.build.flash_mode': 'dio',
			}
	},
	{
		'short': 'espino',
		'name': 'ESPino (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			'.menu.FlashMode.dio.build.flash_mode': 'dio',
			'.menu.FlashMode.qio.build.flash_mode': 'qio',
			}
	},
	{
		'short': 'espinotee',
		'name': 'ThaiEasyElec\'s ESPino',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			}
	},
	{
		'short': 'wifinfo',
		'name': 'WifInfo',
		'opts': {
			'.build.board': 'WIFINFO',
			'.menu.ESPModule.ESP12.build.board': 'ESP8266_ESP12',
			'.menu.FlashMode.dio.build.flash_mode': 'dio',
			'.menu.FlashMode.qio.build.flash_mode': 'qio',
			}
	},
	{
		'short': 'coredev',
		'name': 'Core Development Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
			'.menu.FlashMode.dio.build.flash_mode': 'dio',
			'.menu.FlashMode.qio.build.flash_mode': 'qio',
			'.menu.FlashMode.dout.build.flash_mode': 'dout',
			'.menu.FlashMode.qout.build.flash_mode': 'qout',
			}
	},
	{
		'short': 'arduino-esp8266',
		'name': 'Arduino',
		'opts': {
			'.build.board': 'ESP8266_ARDUINO',
			'.menu.BoardModel.starottodeved.build.board': 'ESP8266_ARDUINO_STAR_OTTO',
			'.menu.BoardModel.primo.build.board': 'ESP8266_ARDUINO_PRIMO',
			'.menu.BoardModel.unowifideved.build.board': 'ESP8266_ARDUINO_UNOWIFI',
			}
	},
	{
		'short': 'gen4iod',
		'name': '4D Systems gen4 IoD Range',
		'opts': {
			'.build.board': 'GEN4_IOD',
			}
	},
	{
		'short': 'oak',
		'name': 'DigiStump Oak',
		'opts': {
			'.build.board': 'ESP8266_OAK',
			'.build.flash_mode': 'dio',
			}
	},
	]


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

	for default in defaults:
		if not ('opts' in board) or not (default[0] in board['opts']):
			print short + default[0] + '=' + default[1]

	if 'opts' in board:
		for opt in board['opts']:
			print short + opt + '=' + board['opts'][opt]
	
	for uspeed in uploadspeed:
		for os in uspeed['os']:
			speed=uspeed['speed']
			print short + '.menu.UploadSpeed.' + str(speed) + os + '=' + str(speed)
			print short + '.menu.UploadSpeed.' + str(speed) + '.upload.speed=' + str(speed)
	
	print ''
