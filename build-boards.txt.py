#!/usr/bin/env python

boards = [
	{
		'short': 'generic',
		'name': 'Generic ESP8266 Module',
	},
	{
		'short': 'esp8285',
		'name': 'Generic ESP8285 Module',
	},
	{
		'short': 'espduino',
		'name': 'ESPDuino (ESP-13 Module)',
	},
	{
		'short': 'huzzah',
		'name': 'Adafruit HUZZAH ESP8266',
	},
	{
		'short': 'espresso_lite_v1',
		'name': 'ESPresso Lite 1.0',
	},
	{
		'short': 'espresso_lite_v2',
		'name': 'ESPresso Lite 2.0',
	},
	{
		'short': 'phoenix_v1',
		'name': 'Phoenix 1.0',
	},
	{
		'short': 'phoenix_v2',
		'name': 'Phoenix 2.0',
	},
	{
		'short': 'nodemcu',
		'name': 'NodeMCU 0.9 (ESP-12 Module)',
	},
	{
		'short': 'nodemcuv2',
		'name': 'NodeMCU 1.0 (ESP-12E Module)',
	},
	{
		'short': 'modwifi',
		'name': 'Olimex MOD-WIFI-ESP8266(-DEV)',
	},
	{
		'short': 'thing',
		'name': 'SparkFun ESP8266 Thing',
	},
	{
		'short': 'thingdev',
		'name': 'SparkFun ESP8266 Thing Dev',
	},
	{
		'short': 'esp210',
		'name': 'SweetPea ESP-210',
	},
	{
		'short': '# wifio',
		'name': 'Wifio',
	},
	{
		'short': 'd1_mini',
		'name': 'WeMos D1 R2 & mini',
	},
	{
		'short': 'd1_mini_lite',
		'name': 'Wemos D1 mini lite (ESP8285)',
	},
	{
		'short': 'd1',
		'name': 'WeMos D1',
	},
	{
		'short': 'espino',
		'name': 'ESPino (ESP-12 Module)',
	},
	{
		'short': 'espinotee',
		'name': 'ThaiEasyElec\'s ESPino',
	},
	{
		'short': 'wifinfo',
		'name': 'WifInfo',
	},
	{
		'short': 'coredev',
		'name': 'Core Development Module',
	},
	{
		'short': 'arduino-esp8266',
		'name': 'Arduino',
	},
	{
		'short': 'gen4iod',
		'name': '4D Systems gen4 IoD Range',
	},
	{
		'short': 'oak',
		'name': 'DigiStump Oak',
	},
	]

serial = [
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

for b in boards:
	print '##############################################################'
	short=b['short']
	print short + '.name=' + b['name']
	print short + '.upload.tool=esptool'
	
	for s in serial:
		for os in s['os']:
			speed=s['speed']
			print short + '.menu.UploadSpeed.' + str(speed) + os + '=' + str(speed)
			print short + '.menu.UploadSpeed.' + str(speed) + '.upload.speed=' + str(speed)
	
	print ''
