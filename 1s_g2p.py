import codecs
import epitran
from epitran.backoff import Backoff

path= "/home/modo/TEFL_asr/"

fileIn = codecs.open(path + "harvardCleanNoPunc.txt", "r")
fileOut = codecs.open(path + "harvard_v0.txt", "w")

backoff = Backoff(['eng-Latn'], cedict_file='cedict_1_0_ts_utf-8_mdbg.txt')


line = fileIn.readline()
phoneLines = []
count= 0

while line:
    count += 1
    print("Processing line", count)

    words = line.strip()
    #print(words)
    words = words.split()

    newLine = []

    for word in words:
        #ipa = backoff.xsampa_list(word)
        ipa= backoff.trans_list(word)
        all_ipa = ""
        for phone in ipa:
            all_ipa += phone

        newLine.append(all_ipa)

    entry = " ".join(newLine)
#    print(entry)
    phoneLines.append(str(entry))

    line = fileIn.readline()

strPhone = "\n".join(phoneLines)

fileOut.write(strPhone)

fileOut.close()
fileIn.close()