import string



print()
print("----- Text Analyzer -----")
panctuation = string.punctuation
while True:
    para = input("Enter your text: ")
    try:
        if para =="":
            print("Enter some input!")
            continue
        else:
            for punc in panctuation:
                para = para.replace(punc,"")
            print()
            print(f"Cleaned Paragraph : {para} ")
            para_list = para.split()
            freq={}
            count = 0
            print()
            print(f'Word Frequencies:')
            for i in para_list:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i]=1
            for word,count in freq.items():
                print(f'{word}: {count}')
            with open("report.txt","a") as f:
                f.write(f'Cleaned Paragraph:\n {para}\n\n')
                f.write("Word Frequencies: \n")
                for  word,count in freq.items():
                    f.write(f'{word}:{count}\n') 
    except:
        print("Enter Some Value!")
        
