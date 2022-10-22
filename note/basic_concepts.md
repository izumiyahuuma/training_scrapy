BASIC CONCEPTSの備忘録  
https://docs.scrapy.org/en/latest/index.html#basic-concepts  

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
## Price validation and dropping items with no prices

Exceptionの項目でも出てくるけど、  
 `raise DropItem()` を呼び出すとそのitemは処理しないことが可能。  

# Feed Exports
スクレイピングした結果を外部へファイル提供とかしたい時に使える機能。  
デフォルトでそういう機能が備わっているので、わざわざファイル書き込みの処理をコーディングしなくてもいいとか。
- `settings.py` に指定された設定を記載する。
  - ここらへんかな？
  - https://docs.scrapy.org/en/latest/topics/feed-exports.html#feeds
- 各出力方法に対応した `ItemExporters` クラスを使う。

また保存先も選べるとか(ローカルはもちろん、S3,GCSなどなど)。

# Requests and Responses
## Request fingerprints
scrapyが過去に収集したページに再度アクセスしないようにするための機構を持っているクラス。  
これがあるおかげで Aページ→Bページ→Aページ→Bページ みたいな無限ループすることを防いでくれる。



