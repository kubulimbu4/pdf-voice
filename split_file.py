

import os
from pikepdf import Pdf

file2pages = {
0: [0, 1],
1: [2, 3],
2: [4, 5],
3: [6, 7],
4: [8, 9],
5: [10, 11],
6: [12, 13],
7: [14, 15],
8: [16, 17],
9: [18, 19],
10: [20, 21],
11: [22, 23],
12: [24, 25],
13: [26, 27],
14: [28, 29],
15: [30, 31],
16: [32, 33],
17: [34, 35],
18: [36, 37],
19: [38, 39],
20: [40, 41],
21: [42, 43],
22: [44, 45],
23: [46, 47],
24: [48, 49],
25: [50, 51],
26: [52, 53],
27: [54, 55],
28: [56, 57],
29: [58, 59],
30: [60, 61],
31: [62, 63],
32: [64, 65],
33: [66, 67],
34: [68, 69],
35: [70, 71]
}

filename = "book.pdf"

pdf = Pdf.open(filename)

new_pdf_files = [ Pdf.new() for i in file2pages ]

new_pdf_index = 0

for n, page in enumerate(pdf.pages):
    if n in list(range(*file2pages[new_pdf_index])):
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
    else:
        # make a unique filename based on original file name plus the index
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-{new_pdf_index}.pdf"
        # save the PDF file
        new_pdf_files[new_pdf_index].save(output_filename)
        print(f"[+] File: {output_filename} saved.")
        # go to the next file
        new_pdf_index += 1
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
              
name, ext = os.path.splitext(filename)
output_filename = f"{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")