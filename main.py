class Genome:
  def __init__(self, inputSequence):
    self.inputSequence = inputSequence.upper()
    self.editSequence = ''

  def display(self):
    inputList = list(self.inputSequence)
    filterList = [x for x in inputList if not determineChar(x)]
    self.editSequence = ''.join(filterList)
    print(self.editSequence)

  def genes(self):
    genes = self.editSequence
    if genes.find('ATG') == -1:
      print('no gene found')
    else:
      split=genes.split('ATG')
      endings = ['TAA','TGA','TAG']
      for j in endings:
        for i in split:
          if len(i) < 3:
            split.remove(i)
        for i in range(len(split)):
          if split[i].find(j)!=-1:
            split[i] = split[i][0:split[i].find(j)]
      for i in split:
        print(i)

def determineChar(inputVal):
  if inputVal != 'A' and inputVal != 'C' and inputVal != 'T' and inputVal != 'G':
    return True

def main():

    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
