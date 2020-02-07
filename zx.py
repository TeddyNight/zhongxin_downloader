import requests
import json
import os
import xmltodict
first=2500
offset=0
data = {"query":"query sectionUserGoods($sectionId: Int!, $first: Int, $offset: Int, $categoryId: Int, $sorting: GoodsSorting, $contentType: ContentType, $period: String){\n    section(id: $sectionId) {\n      type\n      name\n      desc\n      bigImg\n      isTagShow\n      topViewMode\n      categorys{\n        id\n        name\n      }\n      periods{\n        key\n        name\n      }\n      subjects(first: $first, offset: $offset){\n        id\n        name\n        desc\n        smallImage\n        subjectNum\n        pageInfo{\n          hasNext\n          totalCount\n        }\n      }\n      userPackage{\n        endTime\n        isExpired\n        leftSeconds\n        package {\n          id\n          name\n          isContainsEntity\n          userDurationList{\n            good{\n              price{\n                selling\n              }\n              packageDuration {\n                duration\n              }\n            }\n          }\n        }\n      }\n      userGoods(first: $first, offset: $offset, categoryId: $categoryId, sorting: $sorting, contentType: $contentType, period: $period){\n        \n  hasRight\n  hasPackageRight\n  studyProgress{\n    chapterId\n    percent\n    currentTime\n    isEnd\n    chapterName\n    chapterStudyProgressList{\n      chapterId\n      percent\n      currentTime\n    }\n  }\n  pageInfo{\n    totalCount\n    hasNext\n  }\n  good{\n  hasFree\n  isFree\n  id\n  goodsNum\n  typeName\n  desc\n  summary\n  recommendation\n  descImage\n  squareImage\n  descType\n  displayTime\n  name\n  image\n  crossImage\n  type\n  resId\n  ownerSum\n  subName\n  bookAuthor\n  resAuthor\n  isOnlyMainland\n  packageDuration{\n    package{\n      isContainsEntity\n    }\n  }\n  book {\n    id\n    cover\n  }\n  entity{\n    stock\n    chaptersShowCount\n  }\n  liveReplay{\n    id\n    name\n    image\n    videoUrl\n    desc\n    content\n    lecturer\n    duration\n    type\n  }\n  videoBook{\n    id\n    name\n    image\n    desc\n    duration\n  }\n  bookResources{\n    briefAudio{\n      id\n      name\n      desc\n      content\n      url\n      duration\n      isFree\n      isLast\n    }\n  }\n  relatedPeople{\n  id\n  name\n  image\n  intro\n}\n  price {\n  id\n  selling\n  reference\n  normal\n  userSelling\n  isSale\n  saleLeftSeconds\n  userSellingWithRequiredExtraGoods\n  promotionPrice\n  promotionPeriod {\n    startTime\n    endTime\n    status\n    promotion {\n      id\n      isTimeLimit\n      periodStartTime\n      periodEndTime\n      soldQuantity\n      limitQuantity\n      status\n    }\n  }\n}\n  course{\n    author\n    isFinished\n    endDate\n    type\n    chapters{\n      hasDesc\n      id\n      name\n      url\n      duration\n      isFree\n      isLast\n    }\n  }\n  summaryAudioBook{\n    name\n    cover\n    duration\n    url\n    id\n  }\n  summaryBook{\n    content\n    chapterList{\n      id\n      name\n      epubPath\n      num\n      isLast\n    }\n  }\n  bookClub{\n    id\n    name\n    author\n    desc\n    content\n    cover\n    url\n    duration\n  }\n  influencerGuideReading {\n    headerImage\n    wechatGroupQrcode\n    isFinished\n    endTime\n    albums {\n      id\n      name\n      image\n      sections {\n        id\n        name\n        audios {\n          id\n          name\n          url\n          duration\n          isFree\n          isLast\n        }\n      }\n    }\n    lecturers {\n      name\n      intro\n      image\n    }\n  }\n  audioBook{\n    isFinished\n    endDate\n    audios{\n      id\n      name\n      url\n      duration\n      isFree\n      isLast\n    }\n  }\n}\n  \n      }\n      subjects(first: $first, offset: $offset){\n        id\n        name\n        desc\n        smallImage\n        subjectNum\n        pageInfo{\n          hasNext\n          totalCount\n        }\n      }\n    }\n  }","variables":{"contentType":"ALL","categoryId":None,"period":"ALL","sorting":"DEFAULT","first":first,"offset":offset,"sectionId":43}}
headers = {'Content-Type': 'application/json'}
r = requests.post('https://v.yunpub.cn/api/graphql', headers=headers,data=json.dumps(data))
num=1
#print(r.json()['data']['section']['userGoods'][1]['good']['goodsNum'])

for i in r.json()['data']['section']['userGoods']:
	#print(i['good']['goodsNum'])
	print(num)
	num=num+1
	data = {"query":"query chapterList($goodsNum: String) {\n          userGood(goodsNum: $goodsNum) {\n            hasRight\n            hasPackageRight\n            isFavorite\n            studyProgress{\n              chapterId\n              chapterName\n              isEnd\n              percent\n              currentPercent\n            }\n            ebookBookmarks{\n              id\n              chapter {\n                id\n                name\n                epubPath\n              }\n              time\n              position\n            }\n            ebookNotes {\n              id\n              chapterId\n              chapterPercent\n              content\n              createTime\n            }\n            good {\n              id\n              goodsNum\n              isFree\n              name\n              freeChapter\n              price{\n                selling\n              }\n              book {\n                id\n                ebookChapterList {\n                  id\n                  name\n                  epubPath\n                }\n              }\n            }\n          }\n        }","variables":{"goodsNum":i['good']['goodsNum'],"goodsId":None}}
	r = requests.post('https://v.yunpub.cn/api/graphql', headers=headers,data=json.dumps(data))
	res = r.json()['data']['userGood']['good']
	print(res['name'])
	curpath = os.getcwd()
	if os.path.exists(curpath + os.path.sep + res['name'] + ".epub"):
		continue
	os.mkdir(curpath + os.path.sep + res['name'])
	newpath = curpath + os.path.sep + res['name'] + "/OEBPS"
	os.mkdir(newpath)
	os.mkdir(newpath+"/Text")
	os.mkdir(newpath+"/Images")
	os.mkdir(newpath+"/Styles")
	os.chdir(newpath)
	#print(r.json()['data']['userGood']['good']['name'])
	#print(res)
	print("下载索引....")
	try:
		url="https://v.yunpub.cn/api/epub/ebook/chapter/"+str(res['book']['ebookChapterList'][0]['id'])+"/"+res['book']['ebookChapterList'][0]['epubPath'].split("/")[0]+"/OEBPS/"
	except:
		os.chdir(curpath)
		os.system("rm -rf \""+res['name']+"\"")
		continue
	r=requests.get(url+"toc.ncx")
	with open("toc.ncx","wb") as code:
        	code.write(r.content)
	r=requests.get(url+"content.opf")
	with open("content.opf","wb") as code:
		code.write(r.content)
	print("下载图片和CSS...")
	if r.status_code == 404:
		os.chdir(curpath)
		os.system("rm -rf \""+res['name']+"\"")
		continue
	package=xmltodict.parse(r.text)['package']
	#print(package['metadata']['manifest']['item'])
	if "manifest" in package.keys():
		if "item" in package['manifest'].keys():
			item=package['manifest']['item']
	else:
		if "meta" in package['metadata'].keys():
			for x in package['metadata']['meta']:
				if "manifest" in x.keys():
					item=x['item']
		if "manifest" in package['metadata'].keys():
			item=package['metadata']['manifest']['item']
	for m in item:
		if '@media-type' in m.keys():
			if(m['@media-type']=="text/css"):
				rr=requests.get(url+m['@href'])
				with open(m['@href'],"wb") as code:
					code.write(rr.content)
			if(m['@media-type'].split("/")[0]=="image"):
                		rr=requests.get(url+m['@href'])
                		with open(m['@href'],"wb") as code:
                        		code.write(rr.content)
	print("下载网页...")
	for j in res['book']['ebookChapterList']:
		epubPath=j['epubPath']
		r = requests.get("https://v.yunpub.cn/api/epub/ebook/chapter/"+str(j['id'])+"/"+epubPath)
		with open("Text/"+epubPath.split("/")[-1], "wb") as code:
			code.write(r.content)
	print("制作epub...")
	os.chdir(curpath + os.path.sep + res['name'])
	os.system("cp -rf ../META-INF ../mimetype .")
	os.system("zip -r ../\""+res['name']+".epub\" .")
	os.chdir(curpath)
	os.system("rm -rf "+res['name'])
	print("完成")
