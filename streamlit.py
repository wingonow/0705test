import aspose.words as aw
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

doc = aw.Document(file)

for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True) :
    paragraph = paragraph.as_paragraph()

    st.write(str(paragraph.list_format.get_list()) + str(paragraph.text))

