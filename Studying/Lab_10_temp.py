import Lab_10_October_18
import glob
if __name__ == "__main__":
    print("---%s---" % "Task 1")
    nes_list = [1, 2, 3, [4, 5, [3, 6], 6, 3, 3, [3, 3, 3]]]
    print(Lab_10_October_18.frequency(nes_list, 3))

    print("---%s---" % "Task 2")
    sent = "Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, " \
           "упражнений и учебных текстов. Для этого созданы другие замечательные учебники. " \
           "У этой книги совсем иная задача."

    sent_syl = Lab_10_October_18.to_syllables_Russian_sentence(sent)

    print("\n".join(sent_syl))
    print(Lab_10_October_18.to_syllables_Russian("фельдъегерь"))

    print("---%s---" % "Task 3")

    with open('./virus.txt', 'w') as f:
        f.write("The first string\n")
        f.write("The second i am a virus string\n")
        f.write("The third i am not a virus string\n")
    with open('./notvirus.txt', 'w') as f:
        f.write("The first string\n")
        f.write("The second i am not a virus string\n")
        f.write("The third i am not a virus string\n")
    files_arr = glob.glob("./*txt")
    print("Txt-files in the directory before virus search\n: ", files_arr)
    Lab_10_October_18.remove_virus("./*.txt")
    files_arr = glob.glob("./*txt")
    print("Txt-files in the directory after virus search\n: ", files_arr)

    print("---%s---" % "Task 4")
    Lab_10_October_18.define_palindrome(98)
    print(Lab_10_October_18.hidden_anagram("random"))
