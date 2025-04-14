import fasttext

# Huấn luyện mô hình
model = fasttext.train_unsupervised(
    input="/workspace/data/data.txt",           # File dữ liệu văn bản
    model="skipgram",           # Hoặc "cbow"
    dim=300,                    # Kích thước vector (thường 100-300)
    epoch=10,                    # Số lần lặp
    lr=0.05,                    # Learning rate
    minCount=1,                 # Bỏ qua từ xuất hiện dưới 5 lần
    wordNgrams=2,               # Sử dụng word n-grams (1-2)
    minn=3, maxn=6,             # Subword n-grams (3-6 ký tự)
    thread=4                    # Số luồng CPU
)

# Lưu mô hình
model.save_model("underthesea_fasttext_model.bin")