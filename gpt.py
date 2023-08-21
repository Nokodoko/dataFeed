#import os
import sys

from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from pydantic.types import DirectoryPath

query = sys.argv[1]
print(query)

loader = DirectoryLoader("~/vimwiki/" glob="*.wiki" )
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
