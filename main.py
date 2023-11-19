###############################################################
# +=========================================================+ #
# |       OCR Converting Image to Text Using Easeocr        | #
# +=========================================================+ #
# | Author   : JOSE TEOTONIO DA SILVA NETO [TEO]            | #
# | Objective: Build a simple ocr image                     | #
# | Version  : 1.0.0.0                                      | #
# +=========================================================+ #
# | Name   | Changed At | Description                       | #
# +=========================================================+ #
# | Teo    | 15/11/2023 | Build Starter Version             | #
# +=========================================================+ #
###############################################################

# +=========================================================+ #
# | Libraries necessaries to execute current project        | #
# +=========================================================+ #
import streamlit as st  #Web App
import easyocr as ocr
from PIL import Image
import numpy as np 
import utils.wordRules as fc

# +=========================================================+ #
# | Page Title of current project                           | #
# +=========================================================+ #
st.set_page_config(
    page_title = "Uso do OCR", 
    page_icon="🗄",
    layout="wide")

st.header("`📂 OCR - Convertendo Imagens Para Texto`")
st.markdown("---")

# +=========================================================+ #
# | Image Uploader Formats Allowed                          | #
# +=========================================================+ #
image = st.file_uploader(label = "Carregue uma imagem aqui:",type=['png','jpg','jpeg'])

# +=========================================================+ #
# | OCR Image Reader Languages To Be User                   | #
# +=========================================================+ #
reader = ocr.Reader(['en', 'pt'],model_storage_directory='.')

# +=========================================================+ #
# | Sentimental Analisys                                    | #
# +=========================================================+ #
def mostrar_analise(texto):
    p_boas, percentual_bom = fc.buscar_palavras_boas (texto)
    p_mas, percentual_mau = fc.buscar_palavras_mas(texto)
    
    if p_boas==0:
        st.warning("Não identificado palavras boas.")
    else:
        st.success("Palavras boas:")
        st.write("{} palavra(s). Representam das palavras do texto: {:.2f}%".format(p_boas, percentual_bom))
    
    if p_mas==0:
        st.warning("Não identificado palavras más.")
    else:
        st.success("Palavras más:")
        st.write("{} palavra(s). Representam das palavras do texto: {:.2f}%".format(p_mas, percentual_mau))

# +=========================================================+ #
# | Proces Image Uploaded                                   | #
# +=========================================================+ #
if image is not None:

    st.markdown("---")
    st.subheader("Conteúdo que será transcrita")
    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🖊 Processando! "):
        result = reader.readtext(np.array(input_image))
        result_text = [] 

        for text in result:
            result_text.append(text[1])
        
        st.markdown("---")
        st.subheader("Trascricão de imagem para texto")
        st.write(result_text)

        st.markdown("---")
        st.subheader("Análise sentimental do conteúdo da transcrição")
        # SHOW STATISTICS
        mostrar_analise(' '.join(result_text))

    st.balloons()
else:
    st.write("Carregar uma imagem")

st.caption("Made with ❤️ by @teonett")
