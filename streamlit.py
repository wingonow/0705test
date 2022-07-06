import aspose.words as aw
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

#loadOptions = aw.loading.TxtLoadOptions()
#loadOptions.detect_numbering_with_whitespaces = True 
#doc = aw.Document(file, loadOptions)

doc=aw.Document(file)

#doc.save(r'C:\Users\liwenjing\Downloads\survey Q\new.html', SaveFormat.Html);

#text = doc.range.text

#st.write(text)

a=doc.save('output.html')

st.download_button(label='通过csv下载问卷脚本',
                           data=a,
                           file_name='问卷脚本.html',
                           mime='html')

plaintext = aw.PlainTextDocument(file)

st.write(plaintext.text.strip())



#st.write(doc.to_string(aw.SaveFormat.TEXT))
paras = doc.get_child_nodes(aw.NodeType.PARAGRAPH, True)
st.write(type(paras))
for para in paras:
    para = para.as_paragraph()
    st.write(doc.range.text)
    if para.list_format.is_list_item:
        st.write(f"This paragraph belongs to list ID# {para.list_format.list.list_id}, number style \"{para.list_format.list_level.number_style}\"")
        st.write(f"\t\"{para.get_text().strip()}\"")

#for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True) :
#    paragraph = paragraph.as_paragraph()
#
#    st.write(str(paragraph.list_format.list_level_number) + str(paragraph))

