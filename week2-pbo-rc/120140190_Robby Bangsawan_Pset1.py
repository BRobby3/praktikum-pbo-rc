import random

class Father:

  def __init__(self):
    self.alleles = self.get_alleles()

  def get_alleles(self):
    alleles = input(
        "Masukkan alel golongan darah Ayah (A, B, AB, atau O): ").upper()
    if alleles not in ["A", "B", "AB", "O"]:
      print("Golongan darah tidak valid. Silakan masukkan A, B, AB, atau O.")
      return self.get_alleles()
    return alleles

class Mother:

  def __init__(self):
    self.alleles = self.get_alleles()

  def get_alleles(self):
    alleles = input(
        "Masukkan alel golongan darah Ibu (A, B, AB, atau O): ").upper()
    if alleles not in ["A", "B", "AB", "O"]:
      print("Golongan darah tidak valid. Silakan masukkan A, B, AB, atau O.")
      return self.get_alleles()
    return alleles

class Child:

  def __init__(self, father, mother):
    self.father_alleles = father.alleles
    self.mother_alleles = mother.alleles
    self.child_alleles = self.inherit_alleles()
    self.blood_type = self.get_blood_type()

  def inherit_alleles(self):
    father_allele = random.choice(self.father_alleles)
    mother_allele = random.choice(self.mother_alleles)
    return [father_allele, mother_allele]

  def get_blood_type(self):
    alleles = "".join(sorted(self.child_alleles))
    if alleles == "AA":
      return "A"
    elif alleles == "AO" or alleles == "OA":
      return "A"
    elif alleles == "BB":
      return "B"
    elif alleles == "BO" or alleles == "OB":
      return "B"
    elif alleles == "AB":
      return "AB"
    elif alleles == "OO":
      return "O"
    else:
      return "Unknown"

def main():
  father = Father()
  mother = Mother()
  child = Child(father, mother)

  print("\nGolongan darah (alel) Ayah:", father.alleles)
  print("Golongan darah (alel) Ibu:", mother.alleles)
  print("Alel Anak:", child.child_alleles)
  print("Golongan darah Anak:", child.blood_type)

if __name__ == "__main__":
  main()
