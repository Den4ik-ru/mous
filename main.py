import time

import pyautogui


def print_hi(i):

    pyautogui.moveTo(20, 81+i*19, 0)
    #pyautogui.click()

ibil = 0
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for ns in range(1, 99999999):
        f = open("myFile1.txt", "r")
        stroka = f.read()
        i = int(stroka.split('"')[1])
        f.close()

        if i != ibil:
            ibil = i
            for num in range(1, 5):
                pyautogui.moveTo(155, 78, 0.1) #низ
                pyautogui.click()
            pyautogui.moveTo(100, 100, 0.01)  # низ
            pyautogui.click()
            for num in range(1, i):
                pyautogui.press('down', interval=0.001)
            time.sleep(20)
        else:
            time.sleep(1)


    #
    # i = 50
    # for num in range(1, 5):
    #     pyautogui.moveTo(160, 110, 0.1) #низ
    #     pyautogui.click()

 #   pyautogui.moveTo(160, 1000, 0) #низ

    # for num in range(1, 49):
    #     if i > 49:
    #         pyautogui.moveTo(160, 1000, 0)
    #         pyautogui.click()
    #         i = i - 49
    #
    # print_hi(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
