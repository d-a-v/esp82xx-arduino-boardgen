#!/usr/bin/env python

macros = {
	'defaults': [
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
		],

	####################### menu.FlashSize
	'512K64': [
		[ '.menu.FlashSize.512K64', '512K (64K SPIFFS)' ],
		[ '.menu.FlashSize.512K64.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K64.build.flash_ld', 'eagle.flash.512k64.ld' ],
		[ '.menu.FlashSize.512K64.build.spiffs_start', '0x6B000' ],
		[ '.menu.FlashSize.512K64.build.spiffs_end', '0x7B000' ],
		[ '.menu.FlashSize.512K64.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.512K64.upload.maximum_size', '434160' ],
		],
	'512K128': [
		[ '.menu.FlashSize.512K128', '512K (128K SPIFFS)' ],
		[ '.menu.FlashSize.512K128.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K128.build.flash_ld', 'eagle.flash.512k128.ld' ],
		[ '.menu.FlashSize.512K128.build.spiffs_start', '0x5B000' ],
		[ '.menu.FlashSize.512K128.build.spiffs_end', '0x7B000' ],
		[ '.menu.FlashSize.512K128.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.512K128.upload.maximum_size', '368624' ],
		],
	'512K0': [
		[ '.menu.FlashSize.512K0', '512K (no SPIFFS)' ],
		[ '.menu.FlashSize.512K0.build.flash_size', '512K' ],
		[ '.menu.FlashSize.512K0.build.flash_ld', 'eagle.flash.512k0.ld' ],
		[ '.menu.FlashSize.512K0.upload.maximum_size', '499696' ],
		],
	'1M512': [
		[ '.menu.FlashSize.1M512', '1M (512K SPIFFS)' ],
		[ '.menu.FlashSize.1M512.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M512.build.flash_ld', 'eagle.flash.1m512.ld' ],
		[ '.menu.FlashSize.1M512.build.spiffs_start', '0x7B000' ],
		[ '.menu.FlashSize.1M512.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M512.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.1M512.upload.maximum_size', '499696' ],
		],
	'1M256': [
		[ '.menu.FlashSize.1M256', '1M (256K SPIFFS)' ],
		[ '.menu.FlashSize.1M256.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M256.build.flash_ld', 'eagle.flash.1m256.ld' ],
		[ '.menu.FlashSize.1M256.build.spiffs_start', '0xBB000' ],
		[ '.menu.FlashSize.1M256.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M256.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M256.upload.maximum_size', '761840' ],
		],
	'1M192': [
		[ '.menu.FlashSize.1M192', '1M (192K SPIFFS)' ],
		[ '.menu.FlashSize.1M192.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M192.build.flash_ld', 'eagle.flash.1m192.ld' ],
		[ '.menu.FlashSize.1M192.build.spiffs_start', '0xCB000' ],
		[ '.menu.FlashSize.1M192.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M192.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M192.upload.maximum_size', '827376' ],
		],
	'1M160': [
		[ '.menu.FlashSize.1M160', '1M (160K SPIFFS)' ],
		[ '.menu.FlashSize.1M160.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M160.build.flash_ld', 'eagle.flash.1m160.ld' ],
		[ '.menu.FlashSize.1M160.build.spiffs_start', '0xD3000' ],
		[ '.menu.FlashSize.1M160.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M160.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M160.upload.maximum_size', '860144' ],
		],
	'1M144': [
		[ '.menu.FlashSize.1M144', '1M (144K SPIFFS)' ],
		[ '.menu.FlashSize.1M144.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M144.build.flash_ld', 'eagle.flash.1m144.ld' ],
		[ '.menu.FlashSize.1M144.build.spiffs_start', '0xD7000' ],
		[ '.menu.FlashSize.1M144.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M144.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M144.upload.maximum_size', '876528' ],
		],
	'1M128': [
		[ '.menu.FlashSize.1M128', '1M (128K SPIFFS)' ],
		[ '.menu.FlashSize.1M128.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M128.build.flash_ld', 'eagle.flash.1m128.ld' ],
		[ '.menu.FlashSize.1M128.build.spiffs_start', '0xDB000' ],
		[ '.menu.FlashSize.1M128.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M128.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M128.upload.maximum_size', '892912' ],
		],
	'1M64': [
		[ '.menu.FlashSize.1M64', '1M (64K SPIFFS)' ],
		[ '.menu.FlashSize.1M64.build.flash_size', '1M' ],
		[ '.menu.FlashSize.1M64.build.flash_ld', 'eagle.flash.1m64.ld' ],
		[ '.menu.FlashSize.1M64.build.spiffs_start', '0xEB000' ],
		[ '.menu.FlashSize.1M64.build.spiffs_end', '0xFB000' ],
		[ '.menu.FlashSize.1M64.build.spiffs_blocksize', '4096' ],
		[ '.menu.FlashSize.1M64.upload.maximum_size', '958448' ],
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
	'4M1M': [
		[ '.menu.FlashSize.4M1M', '4M (1M SPIFFS)' ],
		[ '.menu.FlashSize.4M1M.build.flash_size', '4M' ],
		[ '.menu.FlashSize.4M1M.build.flash_ld', 'eagle.flash.4m1m.ld' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_start', '0x300000' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_end', '0x3FB000' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.4M1M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.4M1M.upload.maximum_size', '1044464' ],
		],
	'4M3M': [
		[ '.menu.FlashSize.4M3M', '4M (3M SPIFFS)' ],
		[ '.menu.FlashSize.4M3M.build.flash_size', '4M' ],
		[ '.menu.FlashSize.4M3M.build.flash_ld', 'eagle.flash.4m.ld' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_end', '0x3FB000' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.4M3M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.4M3M.upload.maximum_size', '1044464' ],
		],
	'8M7M': [
		[ '.menu.FlashSize.8M7M', '8M (7M SPIFFS)' ],
		[ '.menu.FlashSize.8M7M.build.flash_size', '8M' ],
		[ '.menu.FlashSize.8M7M.build.flash_ld', 'eagle.flash.8m.ld' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_end', '0x7FB000' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.8M7M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.8M7M.upload.maximum_size', '1044464' ],
		],
	'16M15M': [
		[ '.menu.FlashSize.16M15M', '16M (15M SPIFFS)' ],
		[ '.menu.FlashSize.16M15M.build.flash_size', '16M' ],
		[ '.menu.FlashSize.16M15M.build.flash_ld', 'eagle.flash.16m.ld' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_start', '0x100000' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_end', '0x17FB000' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_pagesize', '256' ],
		[ '.menu.FlashSize.16M15M.build.spiffs_blocksize', '8192' ],
		[ '.menu.FlashSize.16M15M.upload.maximum_size', '1044464' ],
		],
	
	
	####################### menu.FlashMode
	'fm_io': [
		[ '.menu.FlashMode.dio', 'DIO' ],
		[ '.menu.FlashMode.dio.build.flash_mode', 'dio' ],
		[ '.menu.FlashMode.qio', 'QIO' ],
		[ '.menu.FlashMode.qio.build.flash_mode', 'qio' ],
		],
	
	'fm_out': [
		[ '.menu.FlashMode.dout', 'DOUT' ],
		[ '.menu.FlashMode.dout.build.flash_mode', 'dout' ],
		[ '.menu.FlashMode.qout', 'QOUT' ],
		[ '.menu.FlashMode.qout.build.flash_mode', 'qout' ],
		],

	}

boards = [
	{
		'short': 'generic',
		'name': 'Generic ESP8266 Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
## flash_mode should be defined elsewhere and merged (in 'opts') where appropriate, how do we easily merge in python?
			},
		'macro': [
			'fm_io', 'fm_out',
			'512K64', '512K128', '512K0', '1M512', '1M256', '1M192', '1M160', '1M144', '1M128', '1M64', '2M', '4M1M', '4M3M',
			],
	},
	{
		'short': 'esp8285',
		'name': 'Generic ESP8285 Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
			'.build.flash_mode': 'dout',
			},
		'macro': [ '1M512', '1M256', '1M192', '1M160', '1M144', '1M128', '1M64' ],
	},
	{
		'short': 'espduino',
		'name': 'ESPDuino (ESP-13 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'huzzah',
		'name': 'Adafruit HUZZAH ESP8266',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'espresso_lite_v1',
		'name': 'ESPresso Lite 1.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V1',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'espresso_lite_v2',
		'name': 'ESPresso Lite 2.0',
		'opts': {
			'.build.board': 'ESP8266_ESPRESSO_LITE_V2',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'phoenix_v1',
		'name': 'Phoenix 1.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V1',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'phoenix_v2',
		'name': 'Phoenix 2.0',
		'opts': {
			'.build.board': 'ESP8266_PHOENIX_V2',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'nodemcu',
		'name': 'NodeMCU 0.9 (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'nodemcuv2',
		'name': 'NodeMCU 1.0 (ESP-12E Module)',
		'opts': {
			'.build.board': 'ESP8266_NODEMCU',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
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
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'd1_mini',
		'name': 'WeMos D1 R2 & mini',
		'opts': {
			'.build.board': 'ESP8266_WEMOS_D1R2MINI',
			'.build.flash_mode': 'dio',
			},
		'macro': [ '4M1M', '4M3M' ],
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
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'espino',
		'name': 'ESPino (ESP-12 Module)',
		'opts': {
			'.build.board': 'ESP8266_ESP12',
			},
		'macro': [
			'fm_io',
			]
	},
	{
		'short': 'espinotee',
		'name': 'ThaiEasyElec\'s ESPino',
		'opts': {
			'.build.board': 'ESP8266_ESP13',
			},
		'macro': [ '4M1M', '4M3M' ],
	},
	{
		'short': 'wifinfo',
		'name': 'WifInfo',
		'opts': {
			'.build.board': 'WIFINFO',
			'.menu.ESPModule.ESP12.build.board': 'ESP8266_ESP12',
			},
		'macro': [
			'fm_io',
			]
	},
	{
		'short': 'coredev',
		'name': 'Core Development Module',
		'opts': {
			'.build.board': 'ESP8266_ESP01',
			},
		'macro': [
			'fm_io', 'fm_out',
			'512K64', '512K128', '512K0', '1M512', '1M256', '1M192', '1M160', '1M144', '1M128', '1M64', '2M', '4M1M', '4M3M', '8M7M', '16M15M'
			],
	},
	{
		'short': 'arduino-esp8266',
		'name': 'Arduino',
		'opts': {
			'.build.board': 'ESP8266_ARDUINO',
			'.menu.BoardModel.starottodeved.build.board': 'ESP8266_ARDUINO_STAR_OTTO',
			'.menu.BoardModel.primo.build.board': 'ESP8266_ARDUINO_PRIMO',
			'.menu.BoardModel.unowifideved.build.board': 'ESP8266_ARDUINO_UNOWIFI',
			},
		'macro': [ '4M1M', '4M3M' ],
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
			},
		'macro': [ '4M1M', '4M3M' ],
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

	# standalone options
	if 'opts' in board:
		for opt in board['opts']:
			print short + opt + '=' + board['opts'][opt]
	
	# macros
	macrolist = [ 'defaults' ]
	if 'macro' in board:
		macrolist += board['macro']
	for block in macrolist:
		for keyval in macros[block]:
			print short + keyval[0] + '=' + keyval[1]

	# serial speed					
	for uspeed in uploadspeed:
		for os in uspeed['os']:
			speed=uspeed['speed']
			print short + '.menu.UploadSpeed.' + str(speed) + os + '=' + str(speed)
			print short + '.menu.UploadSpeed.' + str(speed) + '.upload.speed=' + str(speed)
	
	print ''
