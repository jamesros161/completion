# complete.py
import sys
import json
import shutil

from os import listdir, walk

class Complete:
	def __init__( self ):
		self.args = sys.argv

		self.save_dirs = {
			"tv.shows" : r"V:\TV_Shows",
			"none"     : r"V:\Downloads"
		}

		self.torrent_data = {
			"name"         : self.args[1].lower().replace( " ", "."),
			"content_path" : self.args[2],
			"root_path"    : self.args[3],
			"category"     : self.args[4].lower().replace( " ", ".")
		}
		self.torrent_data["category"] = self.getCategory()

		self.parseContents()

	def getCategory( self ):
		category = 'none'

		if ( 0 < len( self.torrent_data["category"] ) and '.' != self.torrent_data["category"] ):
			category = self.torrent_data["category"]

		return category

	def printData( self ):
		for _, data in self.torrent_data.items():
			print ( data )

	def parseContents( self ):
		is_multi_pack = False
		for ( path, directory, files ) in walk( self.torrent_data['content_path'] ):
			if 0 < len( directory ):
				for directory_name in directory:
					if 'sample' in directory_name.lower():
						continue
					elif 'screens' in directory_name.lower():
						continue
					else:
						is_multi_pack = True

			if is_multi_pack:
				break

			for file_name in files:
				if 'sample' in file_name:
					continue
				if file_name.endswith( '.mkv' ):
					self.movePrimaryFile( [ path, file_name ] )
		if is_multi_pack:
			self.parseMultiPack()

	def movePrimaryFile( self, file_info ):
		src = file_info[0] + '/' + file_info[1]
		if self.torrent_data['category'] in self.save_dirs.keys():
			dest = self.save_dirs[self.torrent_data['category']]
		else:
			dest = self.save_dirs['none']

		shutil.copy( src, dest )

		with open( file_info[0] + '/COPIED', 'w+' ) as fp:
			json.dump( {
				'status' : 'copied',
				'src'    : src,
				'dest'   : dest
			}, fp )


	def parseMultiPack( self ):
		print ( 'coming soon' )

complete = Complete()
input('Press ENTER to exit')
