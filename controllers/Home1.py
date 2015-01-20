#coding:utf-8
import sys
import os.path
import tornado.httpserver
import tornado.web
import tornado.ioloop
import MongoConn
from bson.objectid import ObjectId

dbconn = MongoConn.DBConn()
conn = None


class BaseHandler(tornado.web.RequestHandler):
        def get_current_user(self):
#                return self.get_secure_cookie("user")
		pass

class IndexHandler(BaseHandler):
        #@tornado.web.authenticated
        def get(self):
                #name = tornado.escape.xhtml_escape(self.current_user)
                #self.render('index.html',username=name)

		#top 5
		#top1 = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle order by id desc limit 1')
		#top4 = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle order by id desc limit 1,5')
		#imgUrl=MysqlQuery().query_select('SELECT imgUrl FROM Articles.topArticle order by id desc limit 1')[0][0]
		#newArticles = MysqlQuery().query_select('SELECT title,shortCut,url,comeTag,imgUrl,readCount,comment,keyWords,addTime FROM Articles.Articles order by id desc')
		
		#self.render('index.html',top1Item = top1,top4Items = top4,articlesItems = newArticles)
		dbconn.connect()
		conn = dbconn.getConn()
		global posts
		posts = conn.igudoo.posts
		postlist = posts.find({'status':1}).sort("createDate",-1).limit(10) 
		#postlist = []
		#for post in postslistdic:
		#	postinfo = [post["title"],post["shortcut"],post["createDate"],post["_id"],post["imgurl"]]
		#	postlist.append(postinfo)
		self.render('index.html',postlist=postlist)


        def post(self):
                pass
class TopHandler(BaseHandler):
	def get(self,postid):
		#reInfo = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle where url="%s"' %(topId))
		#self.render('top.html')
		#self.render('top.html',topid=topId,info=reInfo)
		pass
	def post(self):
		#self.render('top.html')
		pass

class NewHandler(BaseHandler):
        def get(self,postid):
		postinfo = posts.find_one({"_id":ObjectId(postid)})
		#postinfolist = [postinfo["title"],postinfo["createDate"],postinfo["postinfo"],postinfo["imgurl"]]
		self.render("post.html",postinfo=postinfo)
                #reInfo = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle where url="%s"' %(articleId))
                #self.render('top.html')
                #self.render('top.html',topid=articleId,info=reInfo)
        def post(self):
                #self.render('top.html')
                pass

if __name__ == "__main__":
                dbconn.connect()
                conn = dbconn.getConn()
                posts = conn.igudoo.posts
                postslistdic = posts.find().sort("create_date",-1).limit(10)
		for post in postslistdic:
			print post
