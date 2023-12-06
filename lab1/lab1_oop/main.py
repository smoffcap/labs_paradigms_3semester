import sys
import math

class Bisquare_equation:
    def __init__(self):
        self.coefficient_A = 0.0
        self.coefficient_B = 0.0
        self.coefficient_C = 0.0
        self.root_num = 0
        self.roots = []

    def get_coef(self, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        while True:
            try:
                coef = float(coef_str)
                break
            except:
                print("Ошибка, вводите число. Попробуйте повторить ввод коэффициента.")
                coef_str = input()
        return coef
    
    def get_coefficients(self):
        self.coefficient_A = self.get_coef(1, "Введите коэффициент A: ")
        self.coefficient_B = self.get_coef(2, "Введите коэффициент B: ")
        self.coefficient_C = self.get_coef(3, "Введите коэффициент C: ")

    def get_roots(self):
        a = self.coefficient_A
        b = self.coefficient_B
        c = self.coefficient_C
        D = b*b - 4*a*c
        if D == 0.0 and (-b / (2.0 * a) > 0):
            root1 = math.sqrt(-b / (2.0 * a))
            root2 = -root1
            self.root_num = 2
            self.roots.append(root1)
            self.roots.append(root2)
        elif D > 0.0:
            sqD = math.sqrt(D)
            pre_root1 = (-b + sqD) / (2.0 * a)
            pre_root2 = (-b - sqD) / (2.0 * a)
            if pre_root1 > 0:
                self.root_num += 2
                self.roots.append(math.sqrt(pre_root1))
                self.roots.append(-math.sqrt(pre_root1))
            if pre_root2 > 0:
                self.root_num += 2
                self.roots.append(math.sqrt(pre_root1))
                self.roots.append(-math.sqrt(pre_root1))    

    def print_roots(self):
        if self.root_num != len(self.roots):
            print("Ошибка, уравнение имеет {} действительных корней, но, согласно результату вычислений {}").format(self.root_num, len((self.roots)))
        else:
            if self.root_num == 0:
                print("Нет корней")
            elif self.root_num == 1:
                print("Один корень: {}".format(self.roots[0]))
            elif self.root_num == 2:
                print("Два корня: {} и {}".format(self.roots[0], self.roots[1]))
            elif self.root_num == 3:
                print("Три корня: {}, {} и {}".format(self.roots[0],self.roots[1],self.roots[2]))
            elif self.root_num == 4:
                print("Четыре корня: {}, {}, {} и {}".format(self.roots[0],self.roots[1],self.roots[2],self.roots[3]))

    
def main():
    q = Bisquare_equation()
    q.get_coefficients()
    q.get_roots()
    q.print_roots()

if __name__ == "__main__":
    main()