from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()

# text = """
# We encourage pinning your version to a specific version in order to avoid breaking your CI when we publish new tests. We recommend upgrading to the latest version periodically to make sure you have the latest tests.

# Not pinning your version will ensure you always have the latest tests, but it may also break your CI if we introduce tests that your integration doesn't pass.
# """

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(docs[0].page_content)
result = splitter.split_documents(docs)

print(result[0].page_content )