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
    while len(genes)>3:
      position = genes.find('ATG')
      printed = False
      if position == -1:
        genes = ''
        if not printed:
          print('no gene found')
      else:
        tempList = list(genes)
        del tempList[0:position+3]
        geneFound = True
        while geneFound:
          list3 = ''.join(tempList[0:3])
          genes = ''.join(tempList)
          if len(list3) > 2 and list3 != 'TAA' and list3 != 'TAG' and list3 != 'TGA':
            if endCheck('TAA',list3,genes) or endCheck('TGA',list3,genes) or endCheck('TAG',list3,genes):
              endings = ['TAA','TAG','TGA']
              for i in range(3):
                if endCheck(endings[i],''.join(tempList[1:3]),genes) or endCheck(endings[i],''.join(tempList[2:4]),genes):
                  del tempList[0:genes.find(endings[i])]
                else:
                  print(list3)
                  del tempList[0:3]
              if genes.find('ATG') != -1:
                del tempList[0:genes.find('ATG')]
              else:
                tempList = []
                genes = ''
                list3 = ''
              list3 = ''.join(tempList[0:3])
              print(list3, end='')
              del tempList[0:3]
              printed = True
          else:
            del tempList[0:genes.find('ATG')+3]
            geneFound = False
            print()
            genes = ''.join(tempList)
            

def determineChar(inputVal):
  if inputVal != 'A' and inputVal != 'C' and inputVal != 'T' and inputVal != 'G':
    return True
def endCheck(ending, string, genes):
  return genes.find(ending) > genes.find(string)

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
