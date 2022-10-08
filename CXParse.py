def parse(input_quote):
    with open('SW3.txt', encoding='utf-8-sig') as f:
        time_array = []
        quote_array = []
        total_line = ""
        count = 1
        for line in f:
            if str(count) == line.replace("\n", ""):
                # print(line)
                count = count + 1
            elif "-->" in line:
                time = line.replace("-->", "to")
                # print("Time is from " + time)
            elif line == '\n':
                quote = total_line
                # print("Quote is: " + quote + "\n")
                total_line = ""
                if input_quote.lower() in quote.lower():
                    time_array.append(time)
                    quote_array.append(quote)
            else:
                x = line.replace("\n", " ")
                if "-" in line:
                    x = x.replace("- ", "")
                total_line += x
        total_array = []
        while len(time_array) != 0:
            total_array.append("Found. At time " + (time_array.pop(0)).replace("\n", "") + " quote is: " + '" ' + quote_array.pop(0) + '"')
        f.close()
        return total_array
