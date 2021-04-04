import sys
from scripts import huffman
from scripts import binary
from scripts import calculator

text = "beebs beepps!!!!! their eerie ears hear pears"
text2 = "pete is here"

print("--------[1]--------")
huffman.buildHuffmanTree(text)


print("\n\n--------[2]--------")
bits1 = binary.toBinary(text)
bitstr1 = str(bits1)
print("Bit length of original ASCII bits: " + str(len(bitstr1)))

compressbitstr = "0101101001011111011010110101110111011110010010010010010111101001001011011000011101000011011100111011000001111011010010110000001111101011000001111"
print("Bit length of compressed: " + str(len(compressbitstr)))

print("Compressed by " + str(calculator.reduction(int(len(bitstr1)), int(len(compressbitstr)))) + " %")

print("\n--------[3]--------")
huffman.buildHuffmanTree(text2)
