import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_openai import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_core.prompts import PromptTemplate, format_document, MessagesPlaceholder
from langchain.tools.retriever import create_retriever_tool
from langchain.tools import Tool
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small") 

chroma_document_store = Chroma( 
    collection_name="chapter8db_hotel_store", 
    embedding_function=embeddings_model, 
    persist_directory="./chapter8db",
)
query = "hotels near Greenwich, London, UK"
similar_documents = chroma_document_store.similarity_search(query=query,k=1)
print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
print(similar_documents)
print("There are", chroma_document_store._collection.count(), "in the collection")

metadata_field_info = [
    AttributeInfo(
        name="HotelRating",
        description="hotel rating One of ['FourStar', 'ThreeStar', 'TwoStar', 'All']",
        type="string",
    ),
    AttributeInfo(
        name="cityName",
        description="Name of the city",
        type="string",
    ),
    AttributeInfo(
        name="countryName",
        description="Name of the country",
        type="string"
    ),
]
document_content_description = "Reviews and Descriptions of hotels"
llm = OpenAI(temperature=0)


retriever = SelfQueryRetriever.from_llm(
        llm,
        chroma_document_store,
        document_content_description,
        metadata_field_info,
        verbose=True,
        search_type='similarity',
        search_kwargs={'k': 10})


template = """you can use the info below to answer questions. 
Helpful Answer: HotelName: {HotelName} CountryName: {countryName} CityName: {cityName} Address: {Address} HotelRating: {HotelRating} HotelWebsite: {HotelWebsiteUrl}\n\n{page_content}"""
  
prompt = PromptTemplate( 
    input_variables=["HotelName", "HotelRating","countryName","cityName","Address", "HotelWebsiteUrl"], 
    template=template, 
) 

hotel_search = create_retriever_tool(
    retriever,
    "provide_hotel_suggestions",
    "Searches and provides hotel suggestions by searching by question and any other metadata, return the Hotel name, Hotel Rating, Hotel City, Hotel Country, Description, Website and a short summary from the metadata. If there are no hotels matching, state that it can't find any hotels with this criteria",
   document_prompt=prompt
)

docs = hotel_search.run(query)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(docs)