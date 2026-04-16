for i in range(1,21):
    with open(f"Tables/table_{i}.txt", "w") as f:
        for n in range(1,11):
            table=f"{i} X {n} = {i*n}\n"
            print(table.strip())
            f.write(table)

    