text = "X-DSPAM-Confidence:    0.8475";
f=text.find('0')
e=text.find('5')
s=slice(f,e+1)
print(float(text[s]))