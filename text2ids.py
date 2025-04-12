from text import text_to_sequence, robust_cleaner, sequence_to_text, basic_cleaner
text = 'Hôm nay nhà hàng chúng tôi khuyến mãi 50% một số sản phẩm, trừ những sản phẩm sau.'

#get ids from raw input text
ids = text_to_sequence(text)
print(ids)

#invert ids to text
txt = sequence_to_text(ids)
print(txt)