import aspose.words as aw
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

#loadOptions = aw.loading.TxtLoadOptions()
#loadOptions.detect_numbering_with_whitespaces = True 
#doc = aw.Document(file, loadOptions)

doc=aw.Document()

#doc.save(r'C:\Users\liwenjing\Downloads\survey Q\new.html', SaveFormat.Html);

#text = doc.range.text

#st.write(text)

#a=doc.save("output.html")
a=doc.save(str)
st.write(a)


#for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True) :
#    paragraph = paragraph.as_paragraph()
#
#    st.write(str(paragraph.list_format.list_level_number) + str(paragraph))

