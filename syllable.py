import string

vowels = "aeiou"

def isLetter(c):
    return (c in string.ascii_letters)

def isVowel(c):
    result = (c in vowels)
    if len(c) != 1:
        for l in c[1:]:
            result = result and (l in vowels)
    return result
    
def isConsonant(c):
    result = (c in string.ascii_letters) and (c not in vowels)
    if len(c) != 1:
        for l in c[1:]:
            result = result and (l in string.ascii_letters) and (l not in vowels)
    return result


def syllablize(s):
    cur_syllable = ""
    syllables = []
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        if cur_syllable != "":
            if isVowel(c):
                if isConsonant(cur_syllable) or isVowel(cur_syllable[-1]):
                    cur_syllable += c
                else:
                    syllables.append(cur_syllable)
                    cur_syllable = c
            elif isConsonant(c):
                # syllable must end with a vowel
                if cur_syllable == "" or isVowel(cur_syllable[-1]):
                    cur_syllable += c
                elif isLetter(c):
                    syllables.append(cur_syllable)
                    cur_syllable = c
            else:
                if cur_syllable != "":
                    syllables.append(cur_syllable)
                    cur_syllable = ""
        elif isLetter(c):
            cur_syllable = c

        i += 1

    return syllables

def formatPrint(s, x = 10):
    i = 0
    j = 0
    n = len(s)
    while i < n:
        if j == 10:
            print(s[i])
            j = 0
        else:
            print(s[i], end=" ")
        j += 1
        i += 1 
s = "The Axis advance halted in 1942 when Japan lost the critical Battle of Midway, near Hawaii, and Germany was defeated in North Africa and then, decisively, at Stalingrad in the Soviet Union. In 1943, with a series of German defeats on the Eastern Front, the Allied invasion of Sicily and the Allied invasion of Italy which brought about Italian surrender, and Allied victories in the Pacific, the Axis lost the initiative and undertook strategic retreat on all fronts. In 1944, the Western Allies invaded German-occupied France, while the Soviet Union regained all of its territorial losses and invaded Germany and its allies. During 1944 and 1945 the Japanese suffered major reverses in mainland Asia in South Central China and Burma, while the Allies crippled the Japanese Navy and captured key Western Pacific islands."

formatPrint(syllablize(s.lower()))

    