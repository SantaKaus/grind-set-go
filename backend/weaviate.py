import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer

img_model = SentenceTransformer('clip-ViT-B-32')
text_model = SentenceTransformer('sentence-transformers/clip-ViT-B-32-multilingual-v1')

# -----------------------------------------------
# CREATE CLIENT
# -----------------------------------------------
# client = weaviate.connect_to_embedded(version="1.23.7")
# client.collections.create(
#     name="Cafe_With_Images",
#     vectorizer_config=wvc.config.Configure.Vectorizer.none(),
#     generative_config=wvc.config.Configure.Generative.openai(),
#     properties=[
#         wvc.config.Property(name="cafe_image1",
#                             data_type=wvc.config.DataType.BLOB),
#         wvc.config.Property(name="cafe_image2",
#                             data_type=wvc.config.DataType.BLOB),
#         wvc.config.Property(name="cafe_image3",
#                             data_type=wvc.config.DataType.BLOB),
#         wvc.config.Property(name="cafe_image4",
#                             data_type=wvc.config.DataType.BLOB),
#         wvc.config.Property(name="cafe_details",
#                             data_type=wvc.config.DataType.TEXT),
#     ])


# -----------------------------------------------
# GET CLIENT
# -----------------------------------------------
cafe_with_images = client.collections.get("Cafe_With_Images")


