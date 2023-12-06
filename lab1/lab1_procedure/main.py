import sys
import math

def get_coef(index, prompt):
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


def get_roots(a, b, c):
    pre_result = []
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        pre_root = -b / (2.0 * a)
        pre_result.append(pre_root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        pre_root1 = (-b + sqD) / (2.0 * a)
        pre_root2 = (-b - sqD) / (2.0 * a)
        pre_result.append(pre_root1)
        pre_result.append(pre_root2)
    for pre_root in pre_result:
        if pre_root > 0:
            result.append(math.sqrt(pre_root))
            result.append(-math.sqrt(pre_root))
        elif pre_root == 0:
            result.append(pre_root)
    return result


def main():
    a = get_coef(1, "Введите коэффициент A: ")
    b = get_coef(2, "Введите коэффициент B: ")
    c = get_coef(3, "Введите коэффициент C: ")

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print("Один корень: {}".format(roots[0]))
    elif len_roots == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))
    
if __name__ == "__main__":
    main()
