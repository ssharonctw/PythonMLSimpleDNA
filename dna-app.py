#webapp built using stramlit and python
#process the user input using panda DataFrame
#visualize the data with altair library

######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt #for the graph
from PIL import Image #python template language

######################
# Page Title
######################

#show the dna logo
image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True) #allow imaeg to extend to the column width

#***shows a horizontal line
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

#sample dna sequence, \n means new line (default of the text input below)
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines() #this will make the input seprated by lines (\n).  Where each line will become an item in the list
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string, with '' linking each of the items

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. use dictionary to show a key-value pair of necleotide and count of nucleotide
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

#Print dictionary
X

### 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
#placing dictionary data to panda's dataframe
#where key of dictionary becomes column header (default) or row header if (orient='index')
df = pd.DataFrame.from_dict(X, orient='index')
#by default, the headers will be zero, hence we can rename it
df = df.rename({0: 'count'}, axis='columns')
#before resetting the index, the index are the dictionary key
#resetting index inplace will make the 0,1,2,3 as new index without creating a new object
df.reset_index(inplace=True)
#renaming the column header 'index' to 'nucleotide'
df = df.rename(columns = {'index':'nucleotide'})
#write the df to streamlit
st.write(df)


### 4. Display Bar Chart using Altair
#.markbar() = set chart to bar chart
#.encode() = the wrapper to set up the x-axis, y-axis, color ...etc
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
