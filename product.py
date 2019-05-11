import os

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:#跳過第一行
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	return products	
	
#使用者輸入
def input_products(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name =='q':		
			break
		price = input('請輸入價格: ')
		products.append([name, price])
	return products

#商品紀錄
def products_information(products):
	for n,p in products:
		print('商品: %s 價格: %s ' %(n,p))

#寫入檔案
def wirte_file(filename, products):
	with open('product.csv','w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for n,p in products:
			f.write('%s,%s\n'  %(n,p)) 


def main():
	filename = input("輸入檔案位置").strip()

	if os.path.isfile(filename): #檢查存不存在
		print("找到檔案了")
		products = read_file(filename)	
	else:
		print('找不到檔案')

	products = input_products(products)
	products_information(products)
	wirte_file(filename, products)

main()