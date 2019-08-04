import xml.etree.ElementTree as ET
import urllib.request as ur

try:
	URL = input('Kindly enter a valid Sitemap url:\n')
except Exception as err:
	print(str(err))
	print('Could not read Sitemap\n')


xml_file = ur.urlopen(URL).read()

filepath = input('\n\nEnter output file folder\n')
filepath = filepath + '/sitemaps_output.txt' 
file = open(filepath,'w+')

xml_parsed = ET.fromstring(xml_file)

my_ns = {'default':'http://www.sitemaps.org/schemas/sitemap/0.9'}


for urls in xml_parsed.findall('default:url',my_ns):
	for locs in urls.findall('default:loc',my_ns):
			file.write(f'{locs.text}\n')

print(f'\n\nOpen file {filepath} to read the output')
file.close()



