import pyperclip

doi = 'https://doi.org/10.1007/s10930-019-09838-3'

bibfile = convert(doi)

#Automatically sends it to your clipboard for pasting
pyperclip.copy(f'{bibfile}')
spam = pyperclip.paste()

# Print result
print(bibfile)
