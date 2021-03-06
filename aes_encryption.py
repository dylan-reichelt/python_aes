import binascii
import numpy
import sys

class aes:
    def __init__(self, key):
        binaryKey = key.encode("utf-8")
        self.key = binaryKey.hex()
        self.sBox = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16)

        self.sBox_inv = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D)
        
        self.rconDict = {
            1: "01000000",
            2: "02000000",
            3: "04000000",
            4: "08000000",
            5: "10000000",
            6: "20000000",
            7: "40000000",
            8: "80000000",
            9: "1b000000",
            10: "36000000",
        }

        self.mixConst = self.makeMatrix("02010103030201010103020101010302")

    # plaintext in hex
    def encrypt(self, plaintext):
        
        encryptedData = ""
        binaryInput = plaintext.encode("utf-8")
        hexInput = binaryInput.hex()
        byteList = []
        tempBytes = ""

        for i in range(len(hexInput)):
            if i % 2 == 0:
                temp = hexInput[i] + hexInput[i + 1]
                tempBytes += temp
        
            if len(tempBytes) == 32:
                byteList.append(tempBytes)
                tempBytes = ""
        
        if tempBytes is not "":
            byteList.append(tempBytes)

        for plaintext in byteList:
            encryptedData += self.encryptRound(plaintext)

        return encryptedData

    def decrypt(self, cyphertext):

        tempBytes = ""
        decryptedText = ""
        for i in range(len(cyphertext)):
            if i % 2 == 0:
                temp = cyphertext[i] + cyphertext[i + 1]
                tempBytes += temp
        
            if len(tempBytes) == 32:
                decryptedText += self.decryptRound(tempBytes)
                tempBytes = ""

        return decryptedText

    # INPUT string rep of hex no 0x at start
    def makeMatrix(self, input1):
        
        listAdd = []
        i = 0
        while i < len(input1):
            if i % 2 == 0:
                listAdd.append(input1[i] + input1[i + 1])
            i += 1
        
        numpyMatrix = numpy.array([ [listAdd[0], listAdd[4], listAdd[8], listAdd[12]], [listAdd[1], listAdd[5], listAdd[9], listAdd[13]], [listAdd[2], listAdd[6], listAdd[10], listAdd[14]], [listAdd[3], listAdd[7], listAdd[11], listAdd[15]] ])

        return numpyMatrix

    # INPUTS: Hex
    def xor(self, input1, input2):
        binary1 = bin(int(input1, 16))[2:].zfill(128) 
        binary2 = bin(int(input2, 16))[2:].zfill(128)
        xor = ""

        i = 0
        while i < len(binary1):
            xor += str(int(binary1[i]) ^ int(binary2[i]))
            i += 1
  
        return hex(int(xor, 2))
    
    # INPUT: matrix 4x4
    def boxSub(self, inputMatrix):
        matCpy = inputMatrix
        i = 0
        j = 0

        for val in numpy.nditer(matCpy):
            decimalValue = int(str(val), 16)
            inputMatrix[i,j] = str(hex(self.sBox[decimalValue]))[2:].zfill(2)
            if j == 3:
                j = 0
                i += 1
                if i == 4:
                    break
            else:
                j += 1
        
        return inputMatrix
    
    def invBoxSub(self, inputMatrix):
        matCpy = inputMatrix
        i = 0
        j = 0

        for val in numpy.nditer(matCpy):
            decimalValue = int(str(val), 16)
            inputMatrix[i,j] = str(hex(self.sBox_inv[decimalValue]))[2:].zfill(2)
            if j == 3:
                j = 0
                i += 1
                if i == 4:
                    break
            else:
                j += 1
        
        return inputMatrix

    # Matrix row input and # of shifts for that row
    def shiftLeft(self, inputBytes, shiftNum):
        cpyInput = inputBytes.copy()
        while shiftNum != 0:

            tempVal = cpyInput[0]
            cpyInput[0] = cpyInput[1]
            cpyInput[1] = cpyInput[2]
            cpyInput[2] = cpyInput[3]
            cpyInput[3] = tempVal
            shiftNum += -1

        return cpyInput
    
    # Matrix row input and # of shifts for that row
    def shiftRight(self, inputBytes, shiftNum):
        cpyInput = inputBytes.copy()
        while shiftNum != 0:

            tempVal = cpyInput[3]
            cpyInput[3] = cpyInput[2]
            cpyInput[2] = cpyInput[1]
            cpyInput[1] = cpyInput[0]
            cpyInput[0] = tempVal
            shiftNum += -1

        return cpyInput

    def roundkey(self, oldKey, round):
        if round == 0:
            return oldKey

        hexList = []
        i = 0
        while i < len(oldKey):
            if i % 2 == 0:
                hexList.append(oldKey[i] + oldKey[i + 1])
            i += 1
        
        w0 = hexList[0:4]
        w1 = hexList[4:8]
        w2 = hexList[8:12]
        w3 = hexList[12:]

        g3 = self.shiftLeft(w3, 1)
        g3 = self.roundBoxSub(g3)
        g3 = str(self.xor(self.rconDict[round], "".join(g3)))[2:].zfill(8)
        
        # multiple xor step
        w4 = str(self.xor("".join(w0), "".join(g3)))[2:].zfill(8)
        w5 = str(self.xor("".join(w1), "".join(w4)))[2:].zfill(8)
        w6 = str(self.xor("".join(w2), "".join(w5)))[2:].zfill(8)
        w7 = str(self.xor("".join(w3), "".join(w6)))[2:].zfill(8)

        returnList = w4 + w5 + w6 + w7
        return "".join(returnList)

    
    def roundBoxSub(self, byteList):
        returnList = []

        for byte in byteList:
            decimalValue = int(str(byte), 16)
            returnList.append(str(hex(self.sBox[decimalValue]))[2:].zfill(2))
        
        return returnList
    
    def mixColumn(self, inputMatrix):
        i = 0
        z = 0

        # Need to make an empty 4x4 numpy matrix for storing the mix column values
        mixMatrix = numpy.empty([4,4], dtype = "<U10")

        while i < 4:
            row = self.mixConst[i,:]
            col = inputMatrix[:,z]

            j = 0
            hexValList = []
            while j < 4:
                hexValList.append(self.galoisMult(int(row[j], 16), int(col[j], 16)))
                j += 1
                
            addValue = 0
            for value in hexValList:
                addValue = self.xor(value, str(addValue))
            mixMatrix[i, z] = addValue[2:].zfill(2)

            if z == 3:
                z = 0
                i += 1
            else:
                z += 1
        
        return(mixMatrix)

    def invMixColumn(self, inputMatrix):

        # Need to make an empty 4x4 numpy matrix for storing the mix column values
        mixMatrix = numpy.empty([4,4], dtype = "<U10")

        i = 0
        while i < 4:
            column = inputMatrix[:,i]
            temp = column.copy()
            column[0] = str(hex(int(self.galoisMult(int(temp[0], 16),14), 16) ^ int(self.galoisMult(int(temp[3], 16),9), 16) ^ \
                        int(self.galoisMult(int(temp[2], 16),13), 16) ^ int(self.galoisMult(int(temp[1], 16),11), 16)))[2:].zfill(2)
            
            column[1] = str(hex(int(self.galoisMult(int(temp[1], 16),14), 16) ^ int(self.galoisMult(int(temp[0], 16),9), 16) ^ \
                        int(self.galoisMult(int(temp[3], 16),13), 16) ^ int(self.galoisMult(int(temp[2], 16),11), 16)))[2:].zfill(2)
            
            column[2] = str(hex(int(self.galoisMult(int(temp[2], 16),14), 16) ^ int(self.galoisMult(int(temp[1], 16),9), 16) ^ \
                        int(self.galoisMult(int(temp[0], 16),13), 16) ^ int(self.galoisMult(int(temp[3], 16),11), 16)))[2:].zfill(2)
            
            column[3] = str(hex(int(self.galoisMult(int(temp[3], 16),14), 16) ^ int(self.galoisMult(int(temp[2], 16),9), 16) ^ \
                        int(self.galoisMult(int(temp[1], 16),13), 16) ^ int(self.galoisMult(int(temp[0], 16),11), 16)))[2:].zfill(2)
            i += 1
        
        return(inputMatrix)

    def galoisMult(self, row, col):
        p = 0
        hiBitSet = 0

        for i in range(8):

            if col & 1 == 1:
                p ^= row

            hiBitSet = row & 0x80
            row <<= 1

            if hiBitSet == 0x80:
                row ^= 0x1b

            col >>= 1
        return hex(p % 256)
    
    def encryptRound(self, sixteenByte):
        #round 0

        xorText = str(self.xor(sixteenByte, self.key))[2:].zfill(32)

        #end round 0
        #rounds 1 - 9
        i = 1
        textState = xorText
        roundKey = self.key
        while i < 10:
            stateMatrix = self.makeMatrix(textState)
            # Step 1: Box substitution
            stateMatrix = self.boxSub(stateMatrix)

            # Step 2: Shifting
            j = 0
            while j < 4:
                stateMatrix[j] = self.shiftLeft(stateMatrix[j,:], j)
                j += 1

            # Step 3: Mix columns
            stateMatrix = self.mixColumn(stateMatrix)

            # Step 4: Round Key XOR
            roundKey = self.roundkey(roundKey, i)
            jumbledText = ""
            t = 0
            while t < 4:
                col = stateMatrix[:,t]
                jumbledText += "".join(col)
                t += 1
            
            textState = str(self.xor(roundKey, jumbledText))[2:].zfill(32)

            i += 1
        
        #end round 1 - 9

        #round 10 (final round)

        # Step 1: Box Sub
        stateMatrix = self.makeMatrix(textState)
        stateMatrix = self.boxSub(stateMatrix)
        
        # Step 2: Shifting
        j = 0
        while j < 4:
            stateMatrix[j] = self.shiftLeft(stateMatrix[j,:], j)
            j += 1

        # Step 3: Round Key XOR
        roundKey = self.roundkey(roundKey, 10)
        jumbledText = ""
        
        i = 0
        while i < 4:
            col = stateMatrix[:,i]
            jumbledText += "".join(col)
            i += 1
            
        textState = str(self.xor(roundKey, jumbledText))[2:].zfill(32)
        return(textState)

        #endround 10

    def decryptRound(self, cyphertext):
        roundkeys = []

        key = self.key
        for i in range(11):
            key = self.roundkey(key, i)
            roundkeys.insert(0, key)
        
        # Round 0

        # Step 1: Xor roundkey 10 and cyphertext
        textState = self.xor(roundkeys[0], cyphertext)[2:].zfill(32)

        # Step 2: shift rows back
        stateMatrix = self.makeMatrix(textState)
        tempValue = 0
        while tempValue < 4:
            stateMatrix[tempValue] = self.shiftRight(stateMatrix[tempValue,:], tempValue)
            tempValue += 1

        # Step 3: inverse-sBox sub
        stateMatrix = self.invBoxSub(stateMatrix)

        # end round 0

        # Round 1 - 9
        tempValue = 1
        while tempValue < 10:
            key = roundkeys[tempValue]
        
            jumbledText = ""
            column = 0
            while column < 4:
                col = stateMatrix[:,column]
                jumbledText += "".join(col)
                column += 1
            
            # Step 1: XOR key and jumbled text
            textState = self.xor(jumbledText, key)[2:].zfill(32)

            # Step 2: Inv MixColumn
            stateMatrix = self.makeMatrix(textState)
            stateMatrix = self.invMixColumn(stateMatrix)

            # Step 3: Shift Rows Right
            shiftvalue = 0
            while shiftvalue < 4:
                stateMatrix[shiftvalue] = self.shiftRight(stateMatrix[shiftvalue,:], shiftvalue)
                shiftvalue += 1

            # Step 4: Inv-SBox Sub
            stateMatrix = self.invBoxSub(stateMatrix)

            tempValue += 1
        
        # End Round 1-9

        # Round 10
        key = roundkeys[len(roundkeys) - 1]
        jumbledText = ""
        for i in range(4):
            col = stateMatrix[:,i]
            jumbledText += "".join(col)
        
        finalHex = self.xor(jumbledText, key)[2:]

        # End Round 10
        finalText = bytes.fromhex(finalHex).decode('utf-8')
        return finalText

        


