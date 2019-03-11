# -*- coding: utf-8 -*-
import scrapy

class LingsearcherSpider(scrapy.Spider):
    
    #Verifica os parametros passados para o spider
    #Pelo nome da loja seta os paths das informacoes do produto
    def __init__(self, store = '', productId = '', **kwargs):
        
        #Aliexpress information
        if store == "aliexpress":
            LingsearcherSpider.store = 'Aliexpress'
            LingsearcherSpider.url = 'https://pt.aliexpress.com/item/xxx/'
            
            #Aliexpress paths
            LingsearcherSpider.productNamePath = '//*[@id="j-product-detail-bd"]/div[1]/div/h1/text()'
            LingsearcherSpider.productPricePath = ['//*[@id="j-sku-price"]/span[1]/text()', '//*[@id="j-sku-discount-price"]/span[1]/text()']
        
        #Dealextreme information
        if store == "dx":
            LingsearcherSpider.store = 'Dealextreme'
            LingsearcherSpider.url = 'https://www.dx.com/p/xxx-'
            
            #Dealextreme paths
            LingsearcherSpider.productNamePath = '/html/body/div[6]/div[2]/div[2]/h1/text()'
            LingsearcherSpider.productPricePath = ['//*[@id="pinfoItemSalePrice"]/dd/span[1]/i[2]/text()']
        
        
        LingsearcherSpider.productId = productId
        self.start_urls = [LingsearcherSpider.url + LingsearcherSpider.productId + '.html']
        self.allowed_domains = ['{}.com'.format(store)]
        super().__init__(**kwargs)
            
    #Information about spider
    name = 'lingsearcherSpider'
    
    def parse(self, response):
        pass
        
        print ("Processing: " + response.url)
        
        productName = response.xpath(LingsearcherSpider.productNamePath).extract()
        price = response.xpath(LingsearcherSpider.productPricePath[0]).extract()
        
        #Verificacao para quando o preco do produto na pagina
        #do aliexpress estiver em promocao, entao, seguir o segundo path
        if (not price):
            price = response.xpath(LingsearcherSpider.productPricePath[1]).extract()
            
        row_data = zip(productName, price)
        
        #Making extracted data row wise
        for item in row_data:
            #Create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'store' : LingsearcherSpider.store,
                'productId' : LingsearcherSpider.productId,
                'page': response.url,
                'productName' : item[0],
                'price' : item[1],
            }
            yield scraped_info
            
    #Id produtos aliexpress 
    #32966289449
    #32922577618
    
    #Id produtos Dealextreme
    #2077881
    
    #Banggood information
    #store = 'Banggood'
    #url = 'http://banggood.com/xxx-p-']
    #productId = '1371927'
    #Banggood paths
    #productNamePath = '//*[@id="centerCtrl"]/div[1]/h2/strong/text()'
    #productPricePath = ['//*[@id="centerCtrl"]/div[5]/div[3]/div[2]/text()']
    
    #Gearbest information
    #store = 'Gearbest'
    #url = 'https://www.gearbest.com/pp_'
    #productId = '009482920417'
    #Gearbest paths
    #productNamePath = '//*[@id="goodsDetail"]/div[2]/div[1]/div[2]/div[1]/h1/text()'
    #productPricePath = '//*[@id="js-panelIntroNormalPrice"]/span[1]/text()'