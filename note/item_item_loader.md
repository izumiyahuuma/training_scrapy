items,item_loaderの備忘録  
https://docs.scrapy.org/en/latest/topics/items.html  
https://docs.scrapy.org/en/latest/topics/loaders.html

# Items
## Item Types
Itemとして認識可能なもののは以下の4つ。  
好きにここらへん選択していいらしい。

- dict
- ItemObjects
- dataclass objects(pythonのdataclassライブラリでデコレートしたもの)
- attrs objects(pythonのattrsライブラリでデコレートしたもの)


# Item_loader
## Using Item Loaders to populate items
ItemLoaderのコンストラクタの引数いくつかあるが、  
topレベルから指定できるんだったらサンプル通りresponseを使えばいい。
selectorから抜き出したいならselectorを指定してやる。
```python
# サンプルはこっち
l = ItemLoader(item=Product(), response=response)
# selectorから指定したい場合はこっち
loader = ItemLoader(item=MyQuoteItem(), selector=hogehoge)
```


## Declaring Item Loaders

loaderの内部の仕組みとしてinput processor,output processorがある。  
- input : `add_xpath()`,`add_csv()`などをされたときに実行される 
- output : `load_item()` した時に実行される

inputで個々のデータに加工を加えて、  
outputで出力前に全てのデータに加工を加えるようなイメージ。  
processorの制御をしたいときにLoaderを作ると良さげみたい。

itemのプロパティ名_in → input processor  
itemのプロパティ名_out → output processor  

関数を指定することで独自のものも実行できるみたい  

# Item Pipeline
