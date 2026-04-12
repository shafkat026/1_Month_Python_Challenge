name=input("Enter your name: \t")
print(f"Good Afternoon, {name}")


letter ='''Dear {name1},
This is to inform you that your application has been successfully processed.
We are pleased to notify you that your joining date is {date}.
Please report on time and bring all necessary documents.
Best regards,  
ABC Company'''

print(letter.replace("{name1}", "Shafkat").replace("{date}","12 April 2026"))


text= "He is a  student"
print(text.find("  "))      #if not found -1
print(text.replace("  ", " "))