import aspose.words as aw
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

doc = aw.Document(file)

text = doc.range.text

#for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True) :
#    paragraph = paragraph.as_paragraph()
#
#    st.write(str(paragraph.list_format.list_level_number) + str(paragraph))

