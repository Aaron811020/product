#讀取檔案
products = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:#跳過第一行
			continue
		name, price = line.strip().split(',')
		products.append([name,price])

#寫入檔案
while True:
	name = input('請輸入商品名稱: ')
	if name =='q':		
		break
	price = input('請輸入價格: ')
	products.append([name, price])

for n,p in products:
	print('商品: %s 價格: %s ' %(n,p))

with open('product.csv','w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for n,p in products:
		f.write('%s,%s\n'  %(n,p)) 