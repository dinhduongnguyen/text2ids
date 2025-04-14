from underthesea import word_tokenize
from text import robust_cleaner
import fasttext
import os
from huggingface_hub import snapshot_download

if not os.path.exists('./assets/underthesea_fasttext_model.bin'):
    print("download model from huggingface hub")
    snapshot_download(
    repo_id='duonguyen/fasttext',
    local_dir='./assets',
    local_dir_use_symlinks=False
    )

model = fasttext.load_model('./assets/underthesea_fasttext_model.bin')

input_text = "Xin chào thế giới năm 2025"

norm_text = robust_cleaner(input_text)
print(norm_text)
norm_text = word_tokenize(norm_text, format="text")
print(norm_text)

embedding = model.get_sentence_vector(norm_text)
print(embedding)
