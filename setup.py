from distutils.core import setup

packages = 	[ 'pathfinding',
		  'pathfinding.algorithms',
		  'pathfinding.classes'
		]

if __name__ == "__main__":

	setup(	
		name='pathfinding',
		version='1.0',
		description='Pathfinding library using graphs',
		author='Jared Welch',
		author_email='jared.welch1@gmail.com',
		packages=packages
	)


