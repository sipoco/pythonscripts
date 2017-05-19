import zipfile, os
# os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
#Old style format

#'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
# =======

# =======
# new style format!
'Compressed file is‘{:.2f}’x smaller!'.format(round(spamInfo.file_size / spamInfo.compress_size, 2))

exampleZip.close()
