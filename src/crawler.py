from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import os
import string
import re
import inflect

engine = inflect.engine()

# Se eliminarion once usuarios por que sus nombres estaban en Chino

def numbersToWordsTransformer(words):

    # This code is for replace numbers with words in user names and maybe in hotel names
    words = words.replace('  ',' ')
    subWords = " ".join(re.split("[A-Za-z]*", words))
    subNumbers = " ".join(re.split("[0-9]*", words))

    print('subwords ',subWords, 'len: ',len(subWords))
    print('subnumber ',subNumbers, 'len: ',len(subNumbers))

    if subWords.isspace():
        subWords = ''


    if len(subWords)>0:
        subWords = list(filter(None,list(map(lambda x: x.replace(' ', ''),subWords.split('  ')))))
        subNumbers = subNumbers.replace('   ', '') #Tres espacios cuando son mas de dos palabras
        subNumbers = subNumbers.replace('  ', ',').replace(' ','')
        subNumbers = list(subNumbers)
        cont = 0
        print(subWords)
        print(subNumbers)
        for changePosition in range(0, len(subNumbers)):
            if subNumbers[changePosition] == ',':
                print(cont)
                subNumbers[changePosition] = engine.number_to_words(int(subWords[cont])).replace(' ','')
                cont = cont + 1

        subNumbers = "".join(subNumbers)

        return subNumbers
    else:
        return words

def charactersAnalisis(hotelAndUserNames):
    #These codes remove stranger characters
    hotelAndUserNames = re.sub("[!@#$%^&*()=+[\];:></?.,_\-'~`]","", hotelAndUserNames)
    hotelAndUserNames = hotelAndUserNames.replace('\\', '')
    hotelAndUserNames = numbersToWordsTransformer(hotelAndUserNames)

    return hotelAndUserNames.lower()


def convertArrayElements():
    sentences = []

    archivoHoteles = open('hotels.txt', 'r')
    archivoNumbers = open('numbers.txt', 'r')

    listaNombresArchivos = os.listdir(r"\Users\Juan\Desktop\Texts\Texts")

    cont = 0
    for (lineHotel, lineNumero) in zip(archivoHoteles.readlines(), archivoNumbers.readlines()):
        fileName = '/Users/Juan/Desktop/Texts/Texts/hotel_' + str(lineNumero) + '_parsed.txt'
        fileName = fileName.replace('\n', '')

        fileTemp = open(fileName, 'r', encoding='utf8')

        for lineHotelFiles in fileTemp.readlines():
            if lineHotelFiles.__contains__('<Author>'):
                getUsers = lineHotelFiles.replace('<Author>', '').replace('\n', '')

                lineHotel = lineHotel.replace('\n', '')

                print(lineNumero)
                print(getUsers)
                print(lineHotel)
                getUsers = charactersAnalisis(getUsers)
                lineHotel = charactersAnalisis(lineHotel)

                tokenizationWords = lineHotel + ' ' + getUsers.replace('  ', '')

                tokenizationWords = tokenizationWords.replace('  ', ' ').split(' ')

                print(tokenizationWords)

                sentences.append(tokenizationWords)

    return sentences

if __name__ == '__main__':

    convertArrayElements()
    # for items in convertArrayElements():
    #     print(items)

    # words = 'holacomovas'
    #
    # subWords = " ".join(re.split("[A-Za-z]*", words))
    # subNumbers = " ".join(re.split("[0-9]*", words))
    #
    # print('subwords ', subWords, len(subWords))
    # print('subnumber ', subNumbers, len(subNumbers))
    #
    # if subWords.isspace():
    #     subWords = ''
    #
    # if subNumbers.isspace():
    #     subNumbers = ''
    #
    # if len(subWords) > 0:
    #     subWords = list(map(lambda x: x.replace(' ', ''), subWords.split('  ')))
    #     subNumbers = subNumbers.replace('  ', ',').replace(' ', '')
    #     subNumbers = list(subNumbers)
    #     cont = 0
    #     for changePosition in range(0, len(subNumbers)):
    #         if subNumbers[changePosition] == ',':
    #             subNumbers[changePosition] = engine.number_to_words(int(subWords[cont])).replace(' ', '')
    #             cont = cont + 1
    #
    #     subNumbers = "".join(subNumbers)
    #
    #     print(subNumbers)
    # else:
    #     print(words)



















    # print(subWords.split('  '))
    # for component in subWords.split('  '):
    #     # print(len(component.replace(' ', '')))
    #     print(component.replace(' ', ''))
    #
    #
    # print('---------------------------------')
    # print(subNumbers.split('  '))
    # for component in subNumbers.split('  '):
    #     print(len(component))
    #     print(component)
