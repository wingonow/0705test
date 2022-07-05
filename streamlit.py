import aspose.words as aw
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

doc = aw.Document(file)

for para in doc.Paragraphs:
    print(para.Range.ListFormat.ListString + str(para))

