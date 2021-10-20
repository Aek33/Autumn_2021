import Lab_10_October_18
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
    print(Lab_10_October_18.to_syllables_Russian("телеобъектив"))
