import aspose.words as aw
import aspose.pydrawing as drawing
import streamlit as st
st.write('hello,world!')

file = st.file_uploader('上传')

#loadOptions = aw.loading.TxtLoadOptions()
#loadOptions.detect_numbering_with_whitespaces = True 
#doc = aw.Document(file, loadOptions)

doc=aw.Document(file)

for list in doc.lists:
    st.write(list)

st.write(help(aspose-words))
    
#doc.update_list_labels()

#paras = [node.as_paragraph() for node in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True)]
## Find if we have the paragraph list. In our document, our list uses plain Arabic numbers,
## which start at three and ends at six.
#for paragraph in paras:
#    if paragraph.list_format.is_list_item:
#        print(f"List item paragraph #{paras.index(paragraph)}")
#        # This is the text we get when getting when we output this node to text format.
#        # This text output will omit list labels. Strip any paragraph formatting characters.
#        paragraph_text = paragraph.to_string(aw.SaveFormat.TEXT).strip()
#        print(f"\tExported Text: {paragraph_text}")
#        label = paragraph.list_label
#        # This gets the position of the paragraph in the current level of the list. If we have a list with multiple levels,
#        # this will tell us what position it is on that level.
#        print(f"\tNumerical Id: {label.label_value}")
#        # Combine them together to include the list label with the text in the output.
#        print(f"\tList label combined with text: {label.label_string} {paragraph_text}")


#doc.save(r'C:\Users\liwenjing\Downloads\survey Q\new.html', SaveFormat.Html);

#text = doc.range.text

#st.write(doc.to_string(aw.SaveFormat.TEXT))

#a=doc.save('output.html')

#st.download_button(label='通过csv下载问卷脚本',
#                           data=a,
#                           file_name='问卷脚本.html',
#                           mime='html')

#plaintext = aw.PlainTextDocument(file)

#st.write(plaintext.text.strip())



#st.write(doc.to_string(aw.SaveFormat.TEXT))
#paras = doc.get_child_nodes(aw.NodeType.PARAGRAPH, True)
#st.write(type(paras))
#for para in paras:
#    para = para.as_paragraph()
#    st.write(doc.range.text)
#    if para.list_format.is_list_item:
#        st.write(f"This paragraph belongs to list ID# {para.list_format.list.list_id}, number style \"{para.list_format.list_level.number_style}\"")
#        st.write(f"\t\"{para.get_text().strip()}\"")

#for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True) :
#    paragraph = paragraph.as_paragraph()
#    st.write(str(paragraph.list_format.list_level_number) + str(paragraph))

