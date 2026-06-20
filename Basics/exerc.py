givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer():
    fmtText = ""
    def __init__(self, text):
        self.text = text.lower()
        list1 = [".", "!", ",", "?"]
        self.fmtText = ""
        for i in list1:
            self.fmtText = self.text = self.text.replace(i, "")

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self, word):
        # return the frequency of a specific word
        return self.freqAll(self.fmtText).get(word, 0)
    

analyzer = TextAnalyzer(givenstring)
print(analyzer.freqAll())
# print(analyzer.freqOf("diam"))