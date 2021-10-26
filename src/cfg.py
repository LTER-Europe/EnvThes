import os

FILE_NAME = os.environ['FILE_NAME']
FDC_CFG = os.environ['FDC_CFG']

file = open(f'{FILE_NAME}.ttl', "r")
ttl = file.read()
file.close()


ttl = ttl.replace("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .", FDC_CFG)
file = open(f'{FILE_NAME}.ttl', "w")
file.write(ttl)
file.close()