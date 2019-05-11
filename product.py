products = []
while True:
	name = input('請輸入商品名稱: ')
	if name =='q':		
		break
	price = input("請輸入價格: ")
	products.append([name, price])

for n,p in products:
	print("商品: %s 價格: %s " %(n,p))

