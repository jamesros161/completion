# complete.py
import sys

from os import listdir

class Complete:
	def __init__( self ):
		self.args = sys.argv
		self.torrent_data = {
			"name"         : self.args[1].lower().replace( " ", "."),
			"content_path" : self.args[2],
			"root_path"    : self.args[3],
			"category"     : self.args[4].lower().replace( " ", ".")
		}
		self.torrent_data["category"] = self.getCategory()

		self.parseContents()

		self.printData()

	def getCategory( self ):
		category = 'None'

		if ( 0 < len( self.torrent_data["category"] ) ):
			category = self.torrent_data["category"]

		return category

	def printData( self ):
		for _, data in self.torrent_data.items():
			print ( data )

	def parseContents( self ):
		contents_walk = {}
		contents_walk = listdir( self.torrent_data['content_path'] )
		print( contents_walk )

complete = Complete()
input('Press ENTER to exit')
