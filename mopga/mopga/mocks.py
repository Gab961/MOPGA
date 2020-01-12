from django.http import Http404

class Post():
	POSTS = [
		{'id':1,'title':'Hello','body':'Salut les loulous, cv?'},
		{'id':2,'title':'Wesh','body':"On m'appelle l'ovni, JCV"},
		{'id':3,'title':'Buongiorno','body':'Come stai mi amore ?'},
		{'id':4,'title':'Halo','body':'Halo teman-teman, selamat datang di blog saya. Semoga harimu menyenangkan!'},
	]


	@classmethod			
	def all(cls):
		return cls.POSTS


	@classmethod
	def findById(cls,id):
		try:
			return cls.POSTS[int(id)-1]
		except:
			raise Http404('Sorry, post #{} not found'.format(id))