def parse(input_quote, num_of_mov):
    with open('../SW' + num_of_mov + '.txt', encoding='utf-8-sig') as f:
        total_line = ""
        count = 1
        total_array = []
        for line in f:
            if str(count) == line.replace("\n", ""):
                count = count + 1
            elif "-->" in line:
                time = line.replace("-->", "to")
            elif line == '\n':
                quote = total_line
                total_line = ""
                if input_quote.lower() in quote.lower():
                    total_array.append("Found. At time " + time.replace("\n", "") + " quote is: " + '" ' + quote + '"')
            else:
                x = line.replace("\n", " ")
                if "-" in line:
                    x = x.replace("- ", "")
                total_line += x
        f.close()
        return total_array
