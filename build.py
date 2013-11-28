#!/usr/bin/python

import os, subprocess

def process(inputname, outputname):
  print(inputname)
  out = subprocess.Popen(["markdown", inputname], stdout=subprocess.PIPE).stdout.read()
  fd = open(outputname, 'w')
  fd.write(
"""<html>
<head>
  <title>Factorization Documentation</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
""")
  fd.write(out)
  fd.write(
"""
</body>
</html>
""")
  fd.close()

for baseName, subDirs, files in os.walk("src/"):
  for inputname in files:
    outputname = "html/" + (inputname.rstrip(".md") + ".html").lstrip("src/")
    inputname = baseName + inputname
    process(inputname, outputname)
