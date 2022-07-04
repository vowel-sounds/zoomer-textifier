import random


def main():
    while True:
        newWords = []
        sent = str(input("type something and i'll zoomerize it:\n"))
        if len(sent) < 1:
            print('thanks for playinggggg')
            break
        words = sent.split()
        if len(words) == 1:
            print('\n\n' + '----------')
            print(zoomerizer(sent) + '\n')
        elif len(words) > 1:
            for x in words:
                if len(x) < 3:
                    newWords.append(x)
                if len(x) >= 3:
                    newWords.append(zoomerizer(x))
            print('\n\n' + '----------')
            print(' '.join(map(str, newWords)) + '\n')


def zoomerizer(sent):
    lastLetter = sent[-1] * random.randint(4, 10)
    return sent + lastLetter


main()
