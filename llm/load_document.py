from langchain.document_loaders import PyPDFLoader



#

def load_pdf(file_path:str):
    loader = PyPDFLoader(file_path)
    return loader.load()


file_extension_handlers = {
    ".pdf": load_pdf,
    # 添加更多的文件后缀名和对应的方法
}